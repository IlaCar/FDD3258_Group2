import matplotlib.pyplot as plt

Avg_time_8  = 0.060722
Std_dev_8   = 0.000283
Avg_time_16 = 0.041539
Std_dev_16  = 0.003894
Avg_time_32 = 0.015602
Std_dev_32  = 0.000011
Avg_time_64 = 0.015720
Std_dev_64  = 0.003408

x_MPI_processes=[8,16,32,64]
y_avg_time=[Avg_time_8,Avg_time_16,Avg_time_32,Avg_time_64]
y_std_dev=[Std_dev_8,Std_dev_16,Std_dev_32,Std_dev_64]

plt.plot(x_MPI_processes, y_avg_time, '--')
plt.errorbar(x_MPI_processes,y_avg_time, yerr=y_std_dev,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')
plt.xlabel('# of MPI processes')
plt.ylabel('mean time (s)')
plt.title('Ex 2 - Q2_1')
plt.grid()
plt.savefig('Ex2_Q2_1.png')

