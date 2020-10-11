#!/bin/bash

# The name of the script is myjob
#SBATCH -J running_hellompi
# Only 1 hour wall-clock time will be given to this job
#SBATCH -t 0:05:00
#SBATCH -A edu20.FDD3258
# Number of nodes
#SBATCH --nodes=1
#SBATCH -e error_file.e

# Run the executable file 
# and write the output into my_output_file
srun -n 4 ./hellompi.out > hellompi_output
