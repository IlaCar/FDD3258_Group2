#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define SEED     921

int main(int argc, char* argv[])
{
  int local_sum = 0, local_count = 0, a, flip = 1 << 24;
  int rank, num_ranks, i, iter, provided;
  double x, y, z, pi;
  double tf[5];
  

  MPI_Init_thread(&argc, &argv, MPI_THREAD_SINGLE, &provided);
  double start_time, stop_time, elapsed_time;
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  MPI_Comm_size(MPI_COMM_WORLD,&num_ranks);
  
  for (int j=0;j<5;j++){
    local_sum = 0; local_count=0;
    if (rank==0){
        start_time = MPI_Wtime();
    }
    
    srand(SEED*rank*(j+1)); // Important: Multiply SEED by "rank" when you introduce MPI!

    double flip_loc = flip/num_ranks;
    // Calculate PI following a Monte Carlo method
    for (int iter = 0; iter < flip_loc; iter++){
        
        // Generate random (X,Y) points
        x = (double)random() / (double)RAND_MAX;
        y = (double)random() / (double)RAND_MAX;
        z = sqrt((x*x) + (y*y));
            
        // Check if point is in unit circle
        if (z <= 1.0){
            local_count++;
        }
    }    
    
    MPI_Reduce(&local_count, &local_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    if (rank==0){
        pi = ((double)local_sum / (double) (flip_loc*num_ranks)) * 4.0;
        stop_time = MPI_Wtime();
        printf("The result is %f\n",pi);
        tf[j] = stop_time - start_time;
    }
    
  }

  MPI_Finalize();

  if (rank==0){
    double mean = (tf[0]+tf[1]+tf[2]+tf[3]+tf[4])/5.0;
    double stdDeviation = sqrt(((tf[0]-mean)*(tf[0]-mean))+((tf[1]-mean)*(tf[1]-mean))+((tf[2]-mean)*(tf[2]-mean))+((tf[3]-mean)*(tf[3]-mean))+((tf[4]-mean)*(tf[4]-mean)))/5.0;
        
    printf("Times are:\n");
    for(int j=0;j<5;j++){
        printf("%f\n",tf[j]);
    }
    printf("Avg time, Std dev: \n%f\n%f\n",mean,stdDeviation);
  }
  return 0;
}

