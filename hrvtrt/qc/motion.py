"""Motion parameters related group statistics."""
from pathlib import Path
import numpy as np
import pandas as pd
import nibabel as nb

import neurokit2 as nk

from ..utils import read_tsv, read_json, parse_bids_subject
from ..hrv import signal_outliers


def data_qc(bids_path, fmriprep_path):
    """
    QC BIDS dataset

    Summarise motion and physiology related QC information.1

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
        fd_mean, fd_max, fd_perc = _fd(fd[1:])

        cii_data = nb.load(str(cii_path)).get_fdata()
        tsnr_mean = _tsnr(cii_data, 0)
        tsnr_mean = None
        qc = {
            "participant_id": subject,
            "session": session,
            "fd_mean": fd_mean,
            "fd_max": fd_max,
            "fd_perc": fd_perc,
            "tsnr_mean": tsnr_mean,
            "cardiac_perc": ppg_out,
            "respiratory_perc": rsp_out,
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
    """Calculate average of temporal signal to noise ratio."""
    meanimg = np.mean(imgdata, axis=t_axis)
    stddevimg = np.std(imgdata, axis=t_axis)
    tsnr = np.zeros_like(meanimg)
    stddevimg_nonzero = stddevimg > 1.0e-3
    tsnr[stddevimg_nonzero] = (
        meanimg[stddevimg_nonzero] / stddevimg[stddevimg_nonzero]
    )
    return np.mean(tsnr)


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
