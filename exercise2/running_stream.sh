#!/bin/bash

# The name of the script is myjob
#SBATCH -J running_myjob
# Only 1 hour wall-clock time will be given to this job
#SBATCH -t 1:00:00
#SBATCH -A edu20.FDD3258
# Number of nodes
#SBATCH --nodes=1
#SBATCH -e error_file.e


# Run the executable file 
# and write the output into my_output_file

for i in 1 2 4 8 12 16 20 24 28 32
do
    export OMP_NUM_THREADS=$i
    for j in 1 2 3 4 5
    do
	NAME="stream_out_n${i}_run${j}"
	srun -n 1 ./my_stream_output > $NAME
    done
done
