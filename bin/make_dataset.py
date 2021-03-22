from pathlib import Path

import pandas as pd

from physiogradient.bids import Phenotype


PROJECT_DIR = Path(__file__).parents[1]
DATADIR = PROJECT_DIR / "data/rawdata/phenotype"
SUBJLIST_PATH = PROJECT_DIR / "data/derivatives/behtrt/participants.tsv"
OUTPUT_PATH = PROJECT_DIR / "data/derivatives/behtrt/"
CODBOOK = DATADIR / "NKI_RS_CODEBOOK.csv"


codebook = pd.read_csv(CODBOOK)[
    ["LORIS_instrument", "loris_variable", "label"]
]

HEADER = {"participant_id": "participant_id", "ses": "association"}

phenotype = Phenotype(DATADIR, SUBJLIST_PATH, HEADER)

data = {}
keep = []
for path in DATADIR.glob("*.tsv"):
    task_name = path.name.split(".")[0]
    var = []
    df = phenotype.parse({task_name: var})
    if  df is not None and df.shape[0] > 40:
        keep.append(task_name)
