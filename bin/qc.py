from hrvtrt.qc import motion
from pathlib import Path
import pandas as pd
import nibabel as nb

from hrvtrt.utils import read_tsv, parse_bids_subject

bids = "/research/cisc1/projects/critchley_nkiphysio/rawdata"
fmriprep = "/research/cisc2/projects/critchley_nkiphysio/derivatives/fmriprep"



def data_qc(bids_path, fmriprep_path):
    """
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
    if type(bids_path) is str:
        bids_path = Path(bids_path)

    if type(fmriprep_path) is str:
        fmriprep_path = Path(fmriprep_path)

    data_paths = fmriprep_path.glob(
        "sub-*/ses-*/func/*_desc-confounds_timeseries.tsv"
    )

    reprot = []
    for confound_path in data_paths:
        subject, session = parse_bids_subject(confound_path.name)
        print(subject, session)
        cii_path = motion._find_cifti(confound_path)
        physio_path = motion._find_physio(subject, session, bids_path)

        # physiology data
        signal, info = motion._physio_process(physio_path)
        ppg_out = motion._outlier_percent(
            signal["PPG_Clean"].values, info["SamplingFrequency"]
        )
        rsp_out = motion._outlier_percent(
            signal["RSP_Clean"].values, info["SamplingFrequency"]
        )

        # populate confounds
        confound_raw = read_tsv(confound_path)
        fd = confound_raw["framewise_displacement"].values
        fd_mean, fd_max, fd_perc = motion._fd(fd[1:])

        cii_data = nb.load(str(cii_path)).get_fdata()
        tsnr_mean = motion._tsnr(cii_data, 0)
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

df = data_qc(bids_path=bids, fmriprep_path=fmriprep)