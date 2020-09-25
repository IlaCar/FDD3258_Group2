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

typedef struct{
    double val;
    int loc;
    char pad[128];    
} tvals;


int main()
{
    int N=1000000;
    double x[N];
    double ti, tf[5];
    
    srand(time(0)); // seed
    for(int i=0; i < N;i++){
        // Generate random number between 0 and 1000
        x[i] = ((double)(rand()) / RAND_MAX)*((double)(rand()) / RAND_MAX)*((double)(rand()) / RAND_MAX)*1;
        //x[i] = i/1000.0;
    }
    double refmaxval = 0.0; int refmaxloc = 0;
    for (int i=0; i < N; i++){
        if (x[i] > refmaxval){
            refmaxval = x[i]; refmaxloc = i;}
    }
    
    int nt;
    #pragma omp parallel
    {
        nt = omp_get_num_threads();
    }
    printf("Number of threads= %d\n",nt);
    
    int mloc;
    double mval;
    tvals maxinfo[nt];
    #pragma omp parallel shared(maxinfo)
    {
        int id = omp_get_thread_num();
        //printf("# thread %d\n",id);
        maxinfo[id].val = -1.0e30;
        #pragma omp for 
        for(int i=0; i < N; i++){
            if (x[i] > maxinfo[id].val){
                    //int id = omp_get_thread_num();
                    maxinfo[id].val = x[i]; maxinfo[id].loc = i;
            }// printf("%f,%d\n",maxval,id);}
        }
    }
    mloc = maxinfo[0].loc;
    mval = maxinfo[0].val;
    //printf("maxima: %f, %f\n",maxval[0],maxval[1]);
    //printf("mval, mloc: %f, %d\n",mval,mloc);
    //printf("nt=%d\n",nt);
    for(int i=1;i<nt;i++){
        if(maxinfo[i].val>mval){
            //printf("here\n");
            mval = maxinfo[i].val;
            mloc = maxinfo[i].loc;
        }
    }
    //printf("max %f, index %d = rmax %f, rindex %d\n",mval,mloc,refmaxval,refmaxloc);
    //printf("max %f, index %d\n",refmaxval,refmaxloc);
    
    const double size=5.0;
    for(int j=0; j<5; j++){
        ti = mysecond();
        int mloc;
        double mval;
        tvals maxinfo[nt];
        #pragma omp parallel shared(maxinfo)
        {
            int id = omp_get_thread_num();
            maxinfo[id].val = -1.0e30;
            #pragma omp for 
            for(int i=0; i < N; i++){
                if (x[i] > maxinfo[id].val){
                        //int id = omp_get_thread_num();
                        maxinfo[id].val = x[i]; maxinfo[id].loc = i;
                }// printf("%f,%d\n",maxval,id);}
            }
        }
        mloc = maxinfo[0].loc;
        mval = maxinfo[0].val;
        for(int i=1;i<nt;i++){
            if(maxinfo[i].val>mval){
                //printf("here\n");
                mval = maxinfo[i].val;
                mloc = maxinfo[i].loc;
            }
        }
        tf[j] = mysecond()-ti;
        //printf("max %f, index %d\n",maxval,maxloc);
        printf("corr: max %f, index %d\n",mval-refmaxval,mloc-refmaxloc);
    }
    double mean = (tf[0]+tf[1]+tf[2]+tf[3]+tf[4])/size;
    double stdDeviation = sqrt(((tf[0]-mean)*(tf[0]-mean))+((tf[1]-mean)*(tf[1]-mean))+((tf[2]-mean)*(tf[2]-mean))+((tf[3]-mean)*(tf[3]-mean))+((tf[4]-mean)*(tf[4]-mean)))/size;
    
    for(int j=0;j<5;j++){
        printf("%f\n",tf[j]);
    }
    printf("Avg time: %f\nStd dev: %f\n",mean,stdDeviation);
    return 0;
}
