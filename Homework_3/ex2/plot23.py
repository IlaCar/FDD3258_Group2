import matplotlib.pyplot as plt

Avg_time_8_21  = 0.060722
Std_dev_8_21   = 0.000283
Avg_time_16_21 = 0.041539
Std_dev_16_21  = 0.003894
Avg_time_32_21 = 0.015602
Std_dev_32_21  = 0.000011
Avg_time_64_21 = 0.015720
Std_dev_64_21  = 0.003408


Avg_time_8_22  = 0.060249
Std_dev_8_22   = 0.000331
Avg_time_16_22 = 0.040059
Std_dev_16_22 = 0.003746
Avg_time_32_22 = 0.015608
Std_dev_32_22  = 0.000004
Avg_time_64_22 = 0.018191
Std_dev_64_22  = 0.004257

Avg_time_8_23  = 0.059238
Std_dev_8_23   = 0.000015
Avg_time_16_23 = 0.042764
Std_dev_16_23  = 0.004355
Avg_time_32_23 = 0.025773
Std_dev_32_23  = 0.000122
Avg_time_64_23 = 0.012784
Std_dev_64_23  = 0.000054



x_MPI_processes=[8,16,32,64]
y_avg_time=[Avg_time_8_23,Avg_time_16_23,Avg_time_32_23,Avg_time_64_23]
y_std_dev=[Std_dev_8_23,Std_dev_16_23,Std_dev_32_23,Std_dev_64_23]

plt.figure()
plt.plot(x_MPI_processes, y_avg_time, '--', color='magenta')
plt.errorbar(x_MPI_processes,y_avg_time, yerr=y_std_dev,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')
plt.xlabel('# of MPI processes')
plt.ylabel('mean time (s)')
plt.title('Ex 2 - Q2_3')
plt.grid()
plt.savefig('Ex2_Q2_3.png')


plt.figure()
y_avg_time_21=[Avg_time_8_21,Avg_time_16_21,Avg_time_32_21,Avg_time_64_21]
y_std_dev_21=[Std_dev_8_21,Std_dev_16_21,Std_dev_32_21,Std_dev_64_21]
y_avg_time_22=[Avg_time_8_22,Avg_time_16_22,Avg_time_32_22,Avg_time_64_22]
y_std_dev_22=[Std_dev_8_22,Std_dev_16_22,Std_dev_32_22,Std_dev_64_22]

plt.plot(x_MPI_processes, y_avg_time_21, '--', label='linear reduction')
plt.errorbar(x_MPI_processes,y_avg_time_21, yerr=y_std_dev_21,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.plot(x_MPI_processes, y_avg_time_22, '--', color='green',label='binary tree reduction')
plt.errorbar(x_MPI_processes,y_avg_time_22, yerr=y_std_dev_22,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.plot(x_MPI_processes, y_avg_time, '--', color='magenta',label='non-blocking - linear reduction')
plt.errorbar(x_MPI_processes,y_avg_time, yerr=y_std_dev,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')


plt.xlabel('# of MPI processes')
plt.ylabel('mean time (s)')
plt.title('Ex 2 - Q2_1 vs Q2_2 vs Q2_3')
plt.grid()
plt.legend()
plt.savefig('Ex2_Q2_1_VS_Q2_2_VS_Q2_3.png')
plt.show()
