from hrvtrt.qc.motion import data_qc

bids = "/research/cisc1/projects/critchley_nkiphysio/rawdata"
fmriprep = "/research/cisc2/projects/critchley_nkiphysio/derivatives/fmriprep"

df = data_qc(bids_path=bids, fmriprep_path=fmriprep)
df.to_csv("/research/cisc2/projects/critchley_nkiphysio/hrvtrt/results/motion_qc.tsv", sep="\t", index=False)
