from ..qc.motion import *
from .utils import get_test_data_path
from pathlib import Path

confounds = (
    Path(get_test_data_path())
    / "sub-test_ses-BAS_task-rest_desc-confounds_timeseries.tsv"
)
