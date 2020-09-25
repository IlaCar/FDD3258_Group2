Question 1.1 

Compile stream.c with OpenMP flag to generate the executable my_stream_output which is run in the bash file running_stream.sh

cc -openmp stream.c -o my_stream_output
sbatch running_stream.sh

Question 1.3

Compile stream.c, stream_static.c and stream_dynamic.c with OpenMP flag to generate the executables my_stream_guided, my_stream_static, my_stream_dynamic which are run in the bash file running_stream_schedule.sh

cc -openmp stream.c -o my_stream_guided
cc -openmp stream_static.c -o my_stream_static
cc -openmp stream_dynamic.c -o my_stream_dynamic
sbatch running_stream_schedule.sh
