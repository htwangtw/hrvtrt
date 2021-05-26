from pathlib import Path

from hrvtrt.download import download

# expecting T1w, T2w, functional, physio file and meta data (8 files) for each session
keywords = ["T1w", "T2w", "task-rest_acq-645"]
n_file = 16

if __name__ == "__main__":
    participants = Path(__file__).parent / "data/participants.tsv"
    localpath = Path(__file__).parent / "data/imaging"
    download(participants, localpath, keywords, n_file=n_file)
