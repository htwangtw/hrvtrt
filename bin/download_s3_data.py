from pathlib import Path
import sys

from hrvtrt.download import download


if __name__ == "__main__":
    participants = Path(__file__).parent / "data/participants.tsv"
    localpath = Path(__file__).parent / "data/imaging"
    # expecting T1w, T2w, functional, physio file and meta data (8 files) for each session
    keywords = ["T1w", "T2w", "task-rest_acq-645"]
    download(participants, localpath, keywords, n_file=16)
