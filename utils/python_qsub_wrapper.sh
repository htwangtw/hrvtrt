# python qsub wrapper for this project
# always execute this script at the root of the repo
# as all files referenced are from here
#
#!/bin/bash
#$ -N pythonjob
#$ -o /home/$USER/logs
#$ -j y
#$ -pe openmp 8
#$ -l m_mem_free=4G


if [[ "x$SGE_ROOT" = "x" ]] ; then
  echo "not on the cluster"
else
  . "${HOME}"/.bash_profile
fi

conda deactivate && conda activate hrvtrt
pip install "${HOME}"/projects/critchley_nkiphysio/hrvtrt/
python "${HOME}"/projects/critchley_nkiphysio/hrvtrt/"${1}"
