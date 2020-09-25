#include "omp.h"
#include "stdio.h"


void main()
{
#pragma omp parallel 
//default number of threads
    {
        int ID = omp_get_thread_num();
        printf("Hello word, I am thread (%d) \n", ID);
    }
}
