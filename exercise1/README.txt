Question 1 

Compile my_hello.c with OpenMP flag to generate the executable my_hello_output which is run in the bash file running_myjob.sh

On Beskow:
cc -openmp my_hello.c -o my_hello_output
sbatch running_myjob.sh

On our laptop, using gcc:
gcc -fopenmp my_hello.c -o my_hello_output
./my_hello_output
