from pathlib import Path
import nibabel as nb
from nilearn import image
from nilearn._utils import check_niimg
import numpy as np


def get_test_data_path():
    return Path(__file__).parent / "data"


def downsample_test_data(prefix):
    """
    Downsampling fmriprep output to create testdata.

    Resolution reduced to 33% of the original.
    Only the first 30 volumes are kept.
    The function is here for book keeping as the real data is not included in the repository.
    The downsampling procedure is modified from on MAIN nilearn tutorial data https://osf.io/wjtyq/
    """
    data = (
        get_test_data_path()
        / "fmriprep"
        / f"{prefix}_task-rest_acq-645_space-MNI152NLin2009cAsym_res-2_desc-preproc_bold.nii.gz"
    )
    mask = (
        get_test_data_path()
        / "fmriprep"
        / f"{prefix}_task-rest_acq-645_space-MNI152NLin2009cAsym_res-2_desc-brain_mask.nii.gz"
    )
    mask = check_niimg(str(mask), atleast_4d=True)
    brain = image.index_img(str(data), slice(0, 30))
    brain = image.math_img("img1*img2", img1=brain, img2=mask)
    aff_orig = nb.load(str(data)).affine[:, -1]
    target_affine = np.column_stack([np.eye(4, 3) * 6, aff_orig])
    downsample_data = image.resample_img(
        brain, target_affine=target_affine, target_shape=(33, 39, 33)
    )
    downsample_data.set_data_dtype("int8")
    nb.save(
        downsample_data,
        str(
            get_test_data_path()
            / "fmriprep"
            / f"{prefix}_task-rest_downsample.nii.gz"
        ),
    )
