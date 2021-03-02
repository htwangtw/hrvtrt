#!/usr/bin/env python
"""
Get TRT subjects' behavioural data
"""
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).parent
DATADIR = PROJECT_DIR / "data/rawdata/phenotype"
SUBJLIST_PATH = PROJECT_DIR / "data/derivatives/behtrt/ses-TRT_subjectinfo.tsv"
OUTPUT_PATH = PROJECT_DIR / "data/derivatives/behtrt/ses-TRT_phenotype.tsv

subject_info = pd.read_csv(SUBJLIST_PATH, sep="\t")

for a in DATADIR.glob("*.tsv"):
    # load participant_id and ses and find match in subject_info

