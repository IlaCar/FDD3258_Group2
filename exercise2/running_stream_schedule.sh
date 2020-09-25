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

export OMP_NUM_THREADS=32
for j in 1 2 3 4 5
do
	NAME="streamout_static_${j}"
	srun -n 1 ./my_stream_static > $NAME
	NAME="streamout_dynamic_${j}"
	srun -n 1 ./my_stream_dynamic > $NAME
	NAME="streamout_guided_${j}"
	srun -n 1 ./my_stream_guided > $NAME
done

