import pytest
from pathlib import Path
import pandas as pd
from ..phenotype import Phenotype, _quicksearch, _parseinfo


test_bids = Path(__file__).parent / "data"

assessment_normal = {
    "assessment1": ["task1_var3", "task1_var5"],
    "assessment2": ["task2_var1"],
}

assessment_missing = {
    "assessment1": ["task1_var3", "task1_var5"],
    "assessment2": ["task2_var1"],
    "assessment3": ["task3_var1"],
}


def test_phenotype_parse():
    info = Phenotype(
        test_bids / "phenotype",
        test_bids / "subject_info.tsv",
        {"participant_id": "subj", "ses": "selected"},
    )
    assert info.session == True
    assert info.index_keys == ["participant_id", "ses"]
    assert info.phenotype_path == test_bids / "phenotype"

    df = info.parse(assessment_normal)
    for n in ["task1_var3", "task1_var5", "task2_var1"]:
        assert n in df.columns

    with pytest.warns(UserWarning) as record:
        df = info.parse(assessment_missing)
    for n in ["task1_var3", "task1_var5", "task2_var1"]:
        assert n in df.columns
    assert "assessment3" in str(record[0].message)


def test_parseinfo():
    info_no_ses = _parseinfo(
        test_bids / "subject_info.tsv", {"participant_id": "subj"}
    )
    assert len(info_no_ses) == 6
    assert info_no_ses["sub-001"] == []

    info = _parseinfo(
        test_bids / "subject_info.tsv",
        {"participant_id": "subj", "ses": "selected"},
    )
    assert len(info) == 6
    assert info["sub-001"] == ["BAS", "TRT"]


def test_quicksearch():
    dirty = pd.DataFrame([{"participant_id": "sub-01", "task": 0}] * 2)
    with pytest.warns(UserWarning) as record:
        empty_ix = _quicksearch(dirty, {"sub-01": []})
    assert "Duplicated" in str(record[0].message)
    assert empty_ix == []
