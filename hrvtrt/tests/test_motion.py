from ..qc.motion import fmri_qc
from .utils import get_test_data_path
from pathlib import Path

fmriprep_path = (
    Path(get_test_data_path())
    / "fmriprep"
)


def test_motion_qc():
    df = fmri_qc(fmriprep_path)
    assert df.shape[0] == 1
    assert df.shape[1] == 6
