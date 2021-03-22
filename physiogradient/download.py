"""
NKI TRT dataset resting state date (TR=645 ms) download script
"""
from pathlib import Path
import os

import pandas as pd

import boto3
from botocore import UNSIGNED
from botocore.client import Config


def get_subjects(datapath):
    df = pd.read_csv(datapath, sep="\t")
<<<<<<< HEAD
    subjects = df.participant_id.tolist()
    baseline = df.baseline.tolist()
    retest = df.retest.tolist()
    sub_ses = []
    for sub, bas, trt in zip(subjects, baseline, retest):
        sub_ses.append((sub, bas))
        sub_ses.append((sub, trt))
=======
    subjects = df.participant_id.unique().tolist()
    sub_ses = []
    for s in subjects:
        list_ses = df.query(f"participant_id=='{s}'").ses.unique().tolist()
        for ses in list_ses:
            sub_ses.append((s, ses))
>>>>>>> main
    return sub_ses


def subject_crawler(subject, session, s3bucket, prefix):
    s3_client = boto3.client("s3", config=Config(signature_version=UNSIGNED))
    bidsfiles = s3_client.list_objects_v2(
        Bucket=s3bucket, Prefix=f"{prefix}/sub-{subject}/ses-{session}/"
    )
    return [d["Key"] for d in bidsfiles["Contents"]]


def keep_file(sub, dt, keep, nfile=14):
    download_these = dt.copy()
    if not download_these.get(sub):
        download_these[sub] = keep
    else:
        download_these[sub] += keep
        if len(download_these[sub]) != nfile:
            download_these.pop(sub)
    return download_these


def filter_files(prefix, files, targetpath):
    keep = []
    local = []
    for f in files:
        if "T1w" in f or "task-rest_acq-645" in f:
            keep.append(f)
            lp = f.replace(prefix, targetpath)
            local.append(lp)
    return list(zip(keep, local))


def creatdir(localpath):
    target = Path(localpath).parent
    if not target.is_dir():
        os.makedirs(target)
        print(target)
