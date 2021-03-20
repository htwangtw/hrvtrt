#!/bin/bash
#$ -N pythonjob
#$ -o /home/$USER/logs
#$ -j y
if [[ "x$SGE_ROOT" = "x" ]] ; then
  echo "not on the cluster"
else
  . ${HOME}/.bash_profile
fi  

conda deactivate && conda activate nki

python ${1}
