#!/bin/bash
#$ -N fmriprep
#$ -pe openmp 8
#$ -o logs
#$ -e logs
#$ -l m_mem_free=4G
#$ -l 'h=!node001&!node069&!node072&!node076&!node077'
#$ -t 1-189
#$ -tc 50

# 189 participants
DATA_DIR=${HOME}/projects/critchley_nkiphysio/scratch/rawdata
SCRATCH_DIR=${HOME}/projects/critchley_nkiphysio/scratch/wd
OUT_DIR=${HOME}/projects/critchley_nkiphysio/derivatives

cd ${DATA_DIR}
SUBJLIST=($(ls sub* -d))
cd ${HOME}

i=$(expr $SGE_TASK_ID - 1)

SUBJECT=${SUBJLIST[${i}]}
echo $SUBJECT

singularity run --cleanenv \
    -B ${DATA_DIR}:/data \
    -B ${OUT_DIR}/:/out \
    -B ${SCRATCH_DIR}:/wd \
    ${HOME}/singularity-images/fmriprep-20.2.1.simg \
    --skip_bids_validation \
    --participant-label ${SUBJECT} \
    --omp-nthreads 4 --nthreads 6 --mem_mb 30000 \
    --longitudinal \
    --output-spaces MNI152NLin2009cAsym:res-2 \
    --fs-license-file ${HOME}/singularity-images/freesurfer_license.txt \
    --work-dir /wd \
    /data /out/ participant

echo Done
