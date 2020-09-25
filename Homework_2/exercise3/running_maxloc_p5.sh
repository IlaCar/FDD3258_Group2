#!/bin/bash

# The name of the script is myjob
#SBATCH -J running_maxloc_p5
# Only 1 hour wall-clock time will be given to this job
#SBATCH -t 0:10:00
#SBATCH -A edu20.FDD3258
# Number of nodes
#SBATCH --nodes=1
#SBATCH -e error_file.e


# Run the executable file 
# and write the output into my_output_file

for i in 1 2 4 8 12 16 20 24 28 32
do
    export OMP_NUM_THREADS=$i
    NAME="maxloc_5_out_n${i}"
    srun -n 1 ./maxloc_p5 > $NAME
done
