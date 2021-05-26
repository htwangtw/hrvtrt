"""Motion parameters related group statistics."""
from pathlib import Path
import numpy as np
import pandas as pd
import nibabel as nb

import neurokit2 as nk

from .utils import read_tsv, read_json, parse_bids_subject
from .hrv import signal_outliers
import matplotlib.pyplot as plt


def plot_qc(path_qc, output_base):
    data = read_tsv(path_qc)

    for qc in ["fd_mean", "fd_max", "fd_perc", "despike_perc", "tsnr_median"]:
        data_to_plot = [
            data[qc][data["session"] != "TRT"].tolist(),
            data[qc][data["session"] == "TRT"].tolist(),
        ]
        plt.figure(figsize=(10, 6))
        x_1 = np.random.normal(1, 0.04, size=int(data.shape[0] / 2))
        x_2 = x_1 + 1
        plt.plot(x_1, data_to_plot[0], "r.", alpha=0.2)
        plt.plot(x_2, data_to_plot[1], "b.", alpha=0.2)
        for x1, x2, y1, y2 in zip(x_1, x_2, data_to_plot[0], data_to_plot[1]):
            plt.plot([x1, x2], [y1, y2], "k-", alpha=0.1)
        box = plt.boxplot(
            data_to_plot,
            positions=[1, 2],
            labels=["Baseline", "Three-week"],
            showfliers=False,
        )
        plt.title(qc)
        plt.savefig(f"{output_base}/results/qc_{qc}.png")


def data_qc(bids_path, fmriprep_path):
    """QC BIDS dataset.

    Summarise motion and physiology related QC information.

    Parameters
    ----------
    bids_path: str or Path
        path to BIDS directory
    fmriprep_path: str or Path
        path to fmriprep derivatives

    Retrun
    ------
    pd.Dataframe
        Individual level fMRI motion QC metrics, including
        Framewise displacement derivatives (mean, maximum, percent above 0.2 mm)
        Mean t-SNR of all  grayordinates
    """
    if isinstance(bids_path, str):
        bids_path = Path(bids_path)

    if isinstance(fmriprep_path, str):
        fmriprep_path = Path(fmriprep_path)

    data_paths = fmriprep_path.glob(
        "sub-*/ses-*/func/*_desc-confounds_timeseries.tsv"
    )

    reprot = []
    for confound_path in data_paths:
        subject, session = parse_bids_subject(confound_path.name)
        print(subject, session)
        cii_path = _find_cifti(confound_path)
        physio_path = _find_physio(subject, session, bids_path)

        # physiology data
        signal, info = _physio_process(physio_path)
        ppg_out = _outlier_percent(
            signal["PPG_Clean"].values, info["SamplingFrequency"]
        )
        rsp_out = _outlier_percent(
            signal["RSP_Clean"].values, info["SamplingFrequency"]
        )

        # populate confounds
        confound_raw = read_tsv(confound_path)
        fd = confound_raw["framewise_displacement"].values
        rmsd = confound_raw["rmsd"].values
        fd_mean, fd_max, fd_perc = _fd(fd[1:], 0.5)
        despike_perc = sum(rmsd > 0.25) / rmsd.shape[0]

        cii_data = nb.load(str(cii_path)).get_fdata()
        tsnr_median = _tsnr(cii_data, 0)
        qc = {
            "participant_id": subject,
            "session": session,
            "fd_mean": fd_mean,
            "fd_max": fd_max,
            "fd_perc": fd_perc,
            "despike_perc": despike_perc,
            "tsnr_median": tsnr_median,
            "cardiac_perc": ppg_out,  # not useful
            "respiratory_perc": rsp_out,  # not useful
        }
        reprot.append(qc)
    return pd.DataFrame(reprot)


def _find_physio(subject, session, bids_path):
    """Get physilogy data from BIDS dataset."""
    physio_path = list(
        bids_path.glob(f"**/sub-{subject}_ses-{session}*_physio.tsv.gz")
    )
    if physio_path and len(physio_path) == 1:
        return physio_path[0]
    else:
        raise ValueError("No associated physiology file")


def _find_cifti(fmriprep_file):
    """Get cifti file path from the relevant confound path."""
    subject, session = parse_bids_subject(fmriprep_file.name)
    cii_path = list(
        fmriprep_file.parent.glob(
            f"sub-{subject}_ses-{session}*_bold.dtseries.nii"
        )
    )
    if cii_path and (len(cii_path) == 1):
        return cii_path[0]
    else:
        raise ValueError(f"No associated cifti file: {fmriprep_file}")


def _tsnr(imgdata, t_axis):
    """Calculate median of temporal signal to noise ratio.
    This is consistent with MRIQC
    """
    meanimg = np.mean(imgdata, axis=t_axis)
    stddevimg = np.std(imgdata, axis=t_axis)
    tsnr = np.zeros_like(meanimg)
    stddevimg_nonzero = stddevimg > 1.0e-3
    tsnr[stddevimg_nonzero] = (
        meanimg[stddevimg_nonzero] / stddevimg[stddevimg_nonzero]
    )
    return np.median(tsnr[tsnr > 0])


def _fd(fd, thresh=0.2):
    """Calculate mean and maximum framewise displacement."""
    if len(fd.shape) != 1:
        raise ValueError("Framewise displacement should has a size of 1 x N")
    fd_mean = np.mean(fd)
    fd_max = np.max(fd)
    fd_perc = sum(fd > thresh) / fd.shape[0]
    return fd_mean, fd_max, fd_perc


def _physio_process(data_path):
    """Basic signal cleaning and peak extraction."""
    json_path = str(data_path).replace("tsv.gz", "json")
    meta = read_json(json_path)
    sampling_rate = meta["SamplingFrequency"]
    data = read_tsv(
        data_path, compression="gzip", names=meta["Columns"], index_col=False
    )
    info = {}
    rsp_signals, rsp_info = nk.rsp_process(data["respiratory"], sampling_rate)
    px_signals, px_info = nk.ppg_process(data["cardiac"], sampling_rate)
    info.update(rsp_info)
    info.update(px_info)
    signal = pd.concat([rsp_signals, px_signals], axis=1)
    signal["time"] = signal.index * 1 / sampling_rate
    signal = signal.set_index("time")
    info["SamplingFrequency"] = sampling_rate
    return signal, info


def _outlier_percent(signal, samping_rate):
    """Percentage of outlier in processed."""
    outliers = signal_outliers(signal, samping_rate)
    return 100 * (sum(outliers) / len(outliers))
