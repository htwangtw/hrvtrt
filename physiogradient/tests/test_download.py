import pytest
from pathlib import Path
from ..download import (
    get_subjects,
    subject_crawler,
    keep_file,
    filter_files,
    creatdir,
)


test_subs = Path(__file__).parent / "data/participants.tsv"


def test_get_subjects():
    sub_ses = get_subjects(test_subs)
    assert len(sub_ses[0]) == 2
<<<<<<< HEAD
    assert len(sub_ses[0][1]) >= 3  # session must be three - 4 char string
=======
    assert sub_ses[0][1] == "TRT"
>>>>>>> main


def test_subject_crawler():
    s3b = "fcp-indi"
    pf = "data/Projects/RocklandSample/RawDataBIDSLatest"
    files = subject_crawler("A00055946", "TRT", s3b, pf)
    assert type(files) == list


def test_keep_file():
    sub = "A00055946"
    dt = {}
    keep = [
        "foo/bar/sub-999_T1w.nii.gz",
        "foo/bar/sub-999_task-rest_acq-645_bold.nii.gz",
        "foo/bar/sub-999_task-rest_acq-645_physio.tsv.gz",
    ]
    # add new subject
    dt = keep_file(sub, dt, keep, nfile=6)
    assert len(dt[sub]) == 3
    # if encounter the subject for a second time and match target
    dt = keep_file(sub, dt, keep, nfile=6)
    assert len(dt[sub]) == 6
    # too many files, remove subject
    dt = keep_file(sub, dt, keep, nfile=6)
    assert len(dt) == 0


def test_filter_files():
    files = [
        "foo/bar/sub-999_T1w.nii.gz",
        "foo/bar/sub-999_task-rest_acq-645_bold.nii.gz",
        "foo/bar/sub-999_task-rest_acq-645_physio.tsv.gz",
        "foo/bar/sub-999_task-rest_acq-1044_bold.nii.gz",
    ]
    targetpath = "/path/to/local"
    source_target_list = filter_files("foo/bar", files, targetpath)
    assert len(source_target_list) == 3
    assert source_target_list[0][1] == f"{targetpath}/sub-999_T1w.nii.gz"


def test_creatdir(tmpdir):
    creatdir(str(tmpdir / "test/files.txt"))
    assert Path(tmpdir / "test").is_dir() == True
