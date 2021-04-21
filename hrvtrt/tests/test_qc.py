from ..qc.motion import data_qc, _physio_process
from .utils import get_test_data_path
from pathlib import Path

fmriprep_path = Path(get_test_data_path()) / "fmriprep"


def test_motion_qc():
    df = data_qc(str(fmriprep_path), str(fmriprep_path))
    assert df.shape[0] == 1
    assert df.shape[1] == 8


def test_physio_process():
    signal, info = _physio_process(
        fmriprep_path
        / "sub-test/ses-BAS/func/sub-test_ses-BAS_task-rest_trimmed_physio.tsv.gz"
    )
    assert signal.shape[-1] == 12
    assert len(info) == 4
