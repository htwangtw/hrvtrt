"""NKI TRT dataset resting state date (TR=645 ms) download script."""
from pathlib import Path
import os
import sys

import boto3
from botocore import UNSIGNED
from botocore.client import Config
import pandas as pd

from .utils import read_tsv


S3BUCKET = "fcp-indi"
PREFIX = "data/Projects/RocklandSample/RawDataBIDSLatest"


def get_subjects(datapath):
    """Get subject and session information form the a specified subset."""
    df = read_tsv(datapath)
    subjects = df.participant_id.tolist()
    baseline = df.baseline.tolist()
    retest = df.retest.tolist()
    sub_ses = []
    for sub, bas, trt in zip(subjects, baseline, retest):
        sub_ses.append((sub, bas))
        sub_ses.append((sub, trt))
    return sub_ses


def subject_crawler(subject, session, s3bucket, prefix):
    """Get AWS S3 path from subect and session information.

    Parameters
    ----------

    subject: str
        Subject ID.

    session: str
        Session ID.

    s3bucket: str
        S3 bucket name

    prefix: str
        Path to the BIDS dataset in the S3 bucket

    Returns
    -------

    List of dict
        S3 path of all files associated with the given subject / session.

    """
    s3_client = boto3.client("s3", config=Config(signature_version=UNSIGNED))
    bidsfiles = s3_client.list_objects_v2(
        Bucket=s3bucket, Prefix=f"{prefix}/sub-{subject}/ses-{session}/"
    )
    return [d["Key"] for d in bidsfiles["Contents"]]


def filter_generate_files(
    s3_prefix,
    target_prefix,
    files,
    keywords=["T1w"],
):
    """Filter files based on keywords, generate target path

    Parameters
    ----------

    s3_prefix, target_prefix: str, str
        Path to BIDS dataset on S3 and your dowload desination

    files: list of str
        List of S3 file paths

    keywords: list of str
        List of keywords you want to keep

    Return
    ------

    List of zipped tuple of source and target path

    """
    s3_keep = []
    local = []
    for f in files:
        for keyword in keywords:
            if keyword in f and (f not in s3_keep):
                print(f)
                target_path = f.replace(s3_prefix, target_prefix)
                s3_keep.append(f)
                local.append(target_path)
    return list(zip(s3_keep, local))


def check_n_files(subject, collector, keep, n_file=1):
    """
    Organise download path per subject for the two sessions.
    If the number of total file is not the same as expected, drop the subject.

    Parameters
    ----------

    subject: str
        Subject ID.

    collecter: dict
        Dictionary collecting files per subject

    keep: list
        List of zipped tuple of source and target path

    n_files: int
        Number of files

    Return
    ------
    dict
        Updated `collecter` dictionary
    """
    download_these = collector.copy()
    if not download_these.get(subject):
        # first session
        download_these[subject] = keep.copy()
    elif len(download_these[subject]) < n_file:
        download_these[subject] += keep.copy()
        if len(download_these[subject]) != n_file:
            download_these.pop(subject)
    return download_these


def creatdir(localpath):
    target = Path(localpath).parent
    if not target.is_dir():
        os.makedirs(target)
        print(target)


def download(participants, local, keywords, n_file):
    """Actual download script"""
    s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))
    sub_ses = get_subjects(participants)
    collector = {}
    for sub, ses in sub_ses:
        files = subject_crawler(sub, ses, s3bucket=S3BUCKET, prefix=PREFIX)
        fit_keywords = filter_generate_files(
            s3_prefix=PREFIX,
            target_prefix=local,
            files=files,
            keywords=keywords,
        )
        collector = check_n_files(sub, collector, fit_keywords, n_file)
    print("gathered all the relevant files")
    print(len(collector))
    for files in collector.values():
        for s, l in files:
            creatdir(l)
            s3.download_file(S3BUCKET, s, l)


if __name__ == "__main__":
    participants = Path(__file__).parent / "data/participants.tsv"
    localpath = sys.argv[1]
    # expecting T1w, T2w, functional, physio file and meta data (8 files) for each session
    keywords = ["T1w", "T2w", "task-rest_acq-645"]
    download(participants, localpath, keywords, n_file=16)
