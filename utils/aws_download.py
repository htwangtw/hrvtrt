from pathlib import Path
import os

import pandas as pd

import boto3
from botocore import UNSIGNED
from botocore.client import Config

S3BUCKET='fcp-indi'
PREFIX='data/Projects/RocklandSample/RawDataBIDSLatest'
LOCAL='/research/cisc1/projects/critchley_nkiphysio/rawdata'
FILEPATH = os.path.dirname(os.path.abspath(__file__))

def get_subjects():
    pwd = Path(FILEPATH)
    df = pd.read_csv(pwd / "nki_trt.tsv", sep="\t")
    subjects = df.participant_id.unique().tolist()
    sub_ses = []
    for s in subjects:
        list_ses = df.query(f"participant_id=='{s}'").ses.unique().tolist()
        for ses in list_ses:
            sub_ses.append((s, ses))
    return sub_ses

def subject_crawler(subject, session):
    s3_client = boto3.client('s3',
                             config=Config(signature_version=UNSIGNED))
    bidsfiles = s3_client.list_objects_v2(
        Bucket=S3BUCKET,
        Prefix=f"{PREFIX}/sub-{subject}/ses-{session}/")
    return [d["Key"] for d in bidsfiles["Contents"]]


def keep_file(sub, dt, keep):
    download_these = dt.copy()
    if not download_these.get(sub):
        download_these[sub] = keep
    else:
        download_these[sub] += keep
        if len(download_these[sub]) != 14:
            download_these.pop(sub)
    return download_these

def filter_files(files):
    keep = []
    local = []
    for f in files:
        if "T1w" in f or "task-rest_acq-645" in f:
            keep.append(f)
            lp = f.replace(PREFIX, LOCAL)
            local.append(lp)
    return list(zip(keep, local))

def main():
    sub_ses = get_subjects()
    download_these = {}
    for sub, ses in sub_ses[:4]:
        files = subject_crawler(sub, ses)
        keep = filter_files(files)
        download_these = keep_file(sub, download_these, keep)

    for files in download_these.values():
        for s, l in files:
            s3.download_file(S3BUCKET, s, l)


if __name__ == "__main__":
    main()
