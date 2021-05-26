from pathlib import Path
from ..download import (
    get_subjects,
    subject_crawler,
    filter_generate_files,
    check_n_files,
    download,
)


test_subs = Path(__file__).parent / "data/participants.tsv"


def test_get_subjects():
    sub_ses = get_subjects(test_subs)
    assert len(sub_ses[0]) == 2
    assert len(sub_ses[0][1]) >= 3  # session must be three - 4 char string


def test_subject_crawler():
    s3b = "fcp-indi"
    pf = "data/Projects/RocklandSample/RawDataBIDSLatest"
    files = subject_crawler("A00055946", "TRT", s3b, pf)
    assert isinstance(files, list) == True


def test_check_n_files():
    sub = "A00055946"
    keep = [
        "foo/bar/sub-999_T1w.nii.gz",
        "foo/bar/sub-999_T2w.nii.gz",
        "foo/bar/sub-999_task-rest_acq-645_bold.nii.gz",
        "foo/bar/sub-999_task-rest_acq-645_physio.tsv.gz",
    ]
    # add new subject
    collector = {}
    collector = check_n_files(sub, collector, keep, n_file=8)
    assert len(collector[sub]) == 4
    # if encounter the subject for a second time and match target
    collector = check_n_files(sub, collector, keep, n_file=8)
    assert len(collector[sub]) == 8

    # too few files, remove subject
    toofew = {}
    toofew = check_n_files(sub, toofew, keep, n_file=8)
    toofew = check_n_files(sub, toofew, keep[:-2], n_file=8)
    assert len(toofew) == 0


def test_filter_generate_files():
    files = [
        "foo/bar/sub-999_T1w.nii.gz",
        "foo/bar/sub-999_T2w.nii.gz",
        "foo/bar/sub-999_task-rest_acq-645_bold.nii.gz",
        "foo/bar/sub-999_task-rest_acq-645_physio.tsv.gz",
        "foo/bar/sub-999_task-rest_acq-1044_bold.nii.gz",  # non existing file
    ]
    targetpath = "/path/to/local"
    source_target_list = filter_generate_files(
        "foo/bar", targetpath, files, keywords=["T1w"]
    )
    assert len(source_target_list) == 1
    assert source_target_list[0][1] == f"{targetpath}/sub-999_T1w.nii.gz"


def test_download(tmpdir):
    download(test_subs, str(tmpdir), keywords=["T1w"], n_file=4)
    assert (
        Path(
            tmpdir
            / "sub-A00018030/ses-FLU1/anat/sub-A00018030_ses-FLU1_T1w.nii.gz"
        ).exists()
        == True
    )
