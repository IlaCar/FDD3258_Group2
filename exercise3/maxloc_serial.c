#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <sys/time.h>
#include <time.h>       /* time */
#include <math.h>

double mysecond()
{
  struct timeval tp;
  struct timezone tzp;
  int i;

  i = gettimeofday(&tp,&tzp);
  return ( (double) tp.tv_sec + (double) tp.tv_usec * 1.e-6 );
}


int main()
{
    int N=1000000;
    double x[N];
    srand(time(0)); // seed
    for(int i=0; i < N;i++){
        // Generate random number between 0 and 1
        x[i] = ((double)(rand()) / RAND_MAX)*((double)(rand()) / RAND_MAX)*((double)(rand()) / RAND_MAX)*1000;
    }
    
    double tf[5];
    const double size=5.0;
    for(int j=0; j<5; j++){
        double ti = mysecond();
        double maxval = 0.0; int maxloc = 0;
        for (int i=0; i < N; i++){
            if (x[i] > maxval) 
                maxval = x[i]; maxloc = i;
        }
        tf[j] = mysecond()-ti;
    }
    double mean = (tf[0]+tf[1]+tf[2]+tf[3]+tf[4])/size;
    double stdDeviation = sqrt(((tf[0]-mean)*(tf[0]-mean))+((tf[1]-mean)*(tf[1]-mean))+((tf[2]-mean)*(tf[2]-mean))+((tf[3]-mean)*(tf[3]-mean))+((tf[4]-mean)*(tf[4]-mean)))/size;
    
    for(int j=0;j<5;j++){
        printf("%f\n",tf[j]);
    }
    printf("Avg time: %f\nStd dev: %f\n",mean,stdDeviation);
    return 0;
}
