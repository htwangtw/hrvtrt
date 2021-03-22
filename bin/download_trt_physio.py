
from physiogradient import download as dl
from pathlib import Path
import boto3
from botocore import UNSIGNED
from botocore.client import Config

S3BUCKET = "fcp-indi"
PREFIX = "data/Projects/RocklandSample/RawDataBIDSLatest"
LOCAL = "/research/cisc1/projects/critchley_nkiphysio/rawdata"
datapath = Path(__file__).parent / "data/participants.tsv"


def main():
    s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))
    sub_ses = dl.get_subjects()
    download_these = {}
    for sub, ses in sub_ses:
        files = dl.subject_crawler(sub, ses, S3BUCKET, PREFIX)
        keep = dl.filter_files(PREFIX, files, LOCAL)
        download_these = dl.keep_file(sub, download_these, keep)
    print("gathered all the relevant files")
    print(len(download_these))
    for files in download_these.values():
        for s, l in files:
            dl.creatdir(l)
            s3.download_file(S3BUCKET, s, l)


if __name__ == "__main__":
    main()
