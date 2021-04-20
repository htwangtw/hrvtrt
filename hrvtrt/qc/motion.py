"""
Motion parameters related group statistics
"""
from pathlib import Path
import numpy as np
import pandas as pd
import nibabel as nb

from ..utils import read_tsv, parse_bids_subject


def fmri_qc(fmriprep_path):
    """
    Summarise motion related QC informations

    Parameters
    ----------
    fmriprep_path: str or Path
        path to fmriprep derivatives

    Retrun
    ------
    pd.Dataframe
        Individual level fMRI motion QC matrics, including
        Framewise displacement derivatives (mean, maximum, percent above 0.2 mm)
        Mean t-SNR of all  grayordinates
    """
    if type(fmriprep_path) is str:
        fmriprep_path = Path(fmriprep_path)

    confound_paths = fmriprep_path.glob(
        "sub-*/ses-*/func/*_desc-confounds_timeseries.tsv"
    )

    motion_qc = []
    for confound_path in confound_paths:
        subject, session = parse_bids_subject(confound_path.name)
        cii_path = _find_cifti(confound_path)
        cii_data = nb.load(str(cii_path)).get_fdata()

        # populate confounds
        confound_raw = read_tsv(confound_path)
        fd = confound_raw["framewise_displacement"].values
        fd_mean, fd_max, fd_perc = _fd(fd[1:])

        cii_data = nb.load(str(cii_path)).get_fdata()
        tsnr_mean = _tsnr(cii_data, 0)
        mq = {
            "participant_id": subject,
            "session": session,
            "fd_mean": fd_mean,
            "fd_max": fd_max,
            "fd_perc": fd_perc,
            "tsnr_mean": tsnr_mean,
        }
        motion_qc.append(mq)
    return pd.DataFrame(motion_qc)


def _find_cifti(confound_path):
    """get cifti file path from the relevant confound path."""
    cii_path = list(confound_path.parent.glob("*_den-91k_bold.dtseries.nii"))
    if cii_path and len(cii_path) == 1:
        return cii_path[0]
    else:
        raise ValueError("No associated cifti file")


def _tsnr(imgdata, t_axis):
    """
    Calculate average of temporal signal to noise ratio.
    """
    meanimg = np.mean(imgdata, axis=t_axis)
    stddevimg = np.std(imgdata, axis=t_axis)
    tsnr = np.zeros_like(meanimg)
    stddevimg_nonzero = stddevimg > 1.0e-3
    tsnr[stddevimg_nonzero] = (
        meanimg[stddevimg_nonzero] / stddevimg[stddevimg_nonzero]
    )
    return np.mean(tsnr)


def _fd(fd, thresh=0.2):
    """
    Calculate mean and maximum framewise displacement.
    """
    if len(fd.shape) != 1:
        raise ValueError("Framewise displacement should has a size of 1 x N")
    fd_mean = np.mean(fd)
    fd_max = np.max(fd)
    fd_perc = sum(fd > thresh) / fd.shape[0]
    return fd_mean, fd_max, fd_perc
