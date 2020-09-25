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
    int N=992870;
    double x[N];
    double ti, tf[5];
    
    srand(time(0)); // seed
    for(int i=0; i < N;i++){
        // Generate random number between 0 and 1000
        x[i] = ((double)(rand()) / RAND_MAX)*((double)(rand()) / RAND_MAX)*((double)(rand()) / RAND_MAX)*1;
    }
    double refmaxval = 0.0; int refmaxloc = 0;
    for (int i=0; i < N; i++){
        if (x[i] > refmaxval){
            refmaxval = x[i]; refmaxloc = i;}
    }
    
    double maxval = 0.0; int maxloc = 0;
    #pragma omp parallel for
    for (int i=0; i < N; i++){
        if (x[i] > maxval){
            maxval = x[i]; maxloc = i;}
    }
    printf("max %f, index %d = rmax %f, rindex %d\n",maxval,maxloc,refmaxval,refmaxloc);
    //printf("max %f, index %d\n",refmaxval,refmaxloc);
    
    const double size=5.0;
    for(int j=0; j<5; j++){
        ti = mysecond();
        maxval = 0.0; maxloc = 0;
        #pragma omp parallel for 
        for(int i=0; i < N; i++){
            if (x[i] > maxval){
                //int id = omp_get_thread_num();
                maxval = x[i]; maxloc = i;}// printf("%f,%d\n",maxval,id);}
        }
        tf[j] = mysecond()-ti;
        //printf("max %f, index %d\n",maxval,maxloc);
        printf("corr: max %f, index %d\n",maxval-refmaxval,refmaxloc-maxloc);
    }
    double mean = (tf[0]+tf[1]+tf[2]+tf[3]+tf[4])/size;
    double stdDeviation = sqrt(((tf[0]-mean)*(tf[0]-mean))+((tf[1]-mean)*(tf[1]-mean))+((tf[2]-mean)*(tf[2]-mean))+((tf[3]-mean)*(tf[3]-mean))+((tf[4]-mean)*(tf[4]-mean)))/size;
    
    for(int j=0;j<5;j++){
        printf("%f\n",tf[j]);
    }
    printf("Avg time: %f\nStd dev: %f\n",mean,stdDeviation);
    return 0;
}
