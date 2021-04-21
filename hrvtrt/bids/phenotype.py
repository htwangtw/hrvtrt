#!/usr/bin/env python

from pathlib import Path
import csv
import warnings
import pandas as pd


class Phenotype:
    """
    Load BIDS phenotype data matching the subject list to a dataframe

    Parameters
    ----------
    phenotype_path : str | Path
        path to BIDS dir `phenotype`

    subject_info : str | Path
        path to the subject info TSV file containing subject number and session info
        one session per row
    header : dict
        relevant header name in subject_info mapped to participant_id and ses
        Example:
            {"participant_id": "<relevant header name in subject_info>",
             "ses": "<relevant header name in subject_info>"}

    Attributes
    ----------
    `phenotype_path` : Path
        path object to BIDS dir `phenotype`

    `subject_info` : dict
        subject number with associated sessions

    `sesssion` : bool
        session information supplied or not

    `index_keys` : list
        keys in assessment file that should be the index
        default: ["participant_id", "ses"]

    """

    def __init__(self, phenotype_path, subject_info, header):
        self.phenotype_path = (
            Path(phenotype_path)
            if isinstance(phenotype_path, str)
            else phenotype_path
        )
        self.subject_info = _parseinfo(subject_info, header)
        self.session = "ses" in header
        self.index_keys = ["participant_id"]
        if self.session:
            self.index_keys.append("ses")

    def parse(self, assessments_info):
        """
        Load assessments

        Parameters
        ----------
        assessments_info: dict
            {"<assessment_name>": ["selected_var1", "selected_var1"]}

        Returns
        -------
        pandas.DataFrame
            selected assessment variables in suplied sample
        """
        collect_data = []
        for assessment, var in assessments_info.items():
            data = self._load_single(assessment, var)
            if data is not None:
                collect_data.append(data)
        if collect_data:
            return pd.concat(collect_data, axis=1)
        else:
            return None

    def _load_single(self, assessment, var=None):
        """
        Load relevant subject and session from one assessment
        set subject and seesion as indices
        """
        df = pd.read_csv(self.phenotype_path / f"{assessment}.tsv", sep="\t")
        idx = _quicksearch(df, self.subject_info, self.session)

        if idx and var:
            return df.loc[idx, self.index_keys.copy() + var].set_index(
                self.index_keys
            )
        elif idx:
            return df.loc[idx, :].set_index(self.index_keys)
        else:
            warnings.warn(
                f"no matching subject with related session {assessment}"
            )


def _parseinfo(path, header):
    """
    Parse subject info
    path:
        path to the subject info TSV file containing subject number and session info
        one session per row
    header:
        header name for subject id and session number in dict
        {"participant_id": "<headername>", "ses": <headername> or None}
    """
    subject_info = {}

    with open(path, "r") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            sub = row[header["participant_id"]]
            if sub not in subject_info:
                subject_info[sub] = []  # add new subject

            if "ses" in header:
                ses = row[header["ses"]]
                subject_info[sub].append(ses)
    return subject_info


def _quicksearch(assessment, subject_info, session=False):
    """
    quick pass on BIDS compatable assesment file to find subject and session
    matched in our list.

    assessement: pd.DataFrame
        assessment data including "participant_id", "ses" in headers
    subject_info:
        dictonanry containing:
            {"<subject-id>": ["<session-name1>", "<session-name2>"]}
    """
    info_header = ["participant_id"]
    if session:
        info_header.append("ses")

    try:
        df = assessment.loc[:, info_header]
    except KeyError:
        raise (KeyError)

    match_index = []
    for sub in subject_info:
        sessions = subject_info[sub]
        search_val = [sub] + sessions
        data_exist = df.isin(search_val).sum(axis=1) == df.shape[1]
        valid_idx = df.index[data_exist].tolist()
        if len(valid_idx) == len(sessions):
            match_index += valid_idx
        elif len(valid_idx) > 1:
            warnings.warn(
                f"Duplicated entry: {search_val}, please check if your raw data is dirty"
            )
    return match_index
