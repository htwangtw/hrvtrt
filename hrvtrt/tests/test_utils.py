from ..utils import read_tsv, parse_bids_subject
from .utils import get_test_data_path

from pathlib import Path
import pytest

test_tsv = Path(get_test_data_path()) / "participants.tsv"


def test_invalid_input():
    """Invalid inputs."""
    with pytest.raises(Exception):
        read_tsv(test_tsv, sep="\t")

    with pytest.raises(ValueError):
        parse_bids_subject("file.tsv")
