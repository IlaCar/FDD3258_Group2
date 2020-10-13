import matplotlib.pyplot as plt

Avg_time_8_21  = 0.060722
Std_dev_8_21   = 0.000283
Avg_time_16_21 = 0.041539
Std_dev_16_21  = 0.003894
Avg_time_32_21 = 0.015602
Std_dev_32_21  = 0.000011
Avg_time_64_21 = 0.015720
Std_dev_64_21  = 0.003408
Avg_time_128_21 = 0.012168
Std_dev_128_21  = 0.005308



Avg_time_8_22  = 0.060249
Std_dev_8_22   = 0.000331
Avg_time_16_22 = 0.040059
Std_dev_16_22 = 0.003746
Avg_time_32_22 = 0.015608
Std_dev_32_22  = 0.000004
Avg_time_64_22 = 0.018191
Std_dev_64_22  = 0.004257
Avg_time_128_22 = 0.013021
Std_dev_128_22  = 0.004147

Avg_time_8_23  = 0.059238
Std_dev_8_23   = 0.000015
Avg_time_16_23 = 0.042764
Std_dev_16_23  = 0.004355
Avg_time_32_23 = 0.025773
Std_dev_32_23  = 0.000122
Avg_time_64_23 = 0.012784
Std_dev_64_23  = 0.000054
Avg_time_128_23 = 0.010716
Std_dev_128_23  = 0.003379

Avg_time_8_24  = 0.060294
Std_dev_8_24   = 0.000385
Avg_time_16_24 = 0.037886
Std_dev_16_24  = 0.003789
Avg_time_32_24 = 0.015621
Std_dev_32_24  = 0.000040
Avg_time_64_24 = 0.018713
Std_dev_64_24  = 0.004739
Avg_time_128_24 = 0.012919
Std_dev_128_24  = 0.004268

Avg_time_8_25  = 0.065967
Std_dev_8_25   = 0.005591
Avg_time_16_25 = 0.040682
Std_dev_16_25  = 0.003588
Avg_time_32_25 = 0.015627
Std_dev_32_25  = 0.000014
Avg_time_64_25 = 0.018792
Std_dev_64_25  = 0.006445
Avg_time_128_24 = 0.008935
Std_dev_128_24  = 0.000084



x_MPI_processes=[8,16,32,64,128]
y_avg_time=[Avg_time_8_25,Avg_time_16_25,Avg_time_32_25,Avg_time_64_25,Avg_time_128_25]
y_std_dev=[Std_dev_8_25,Std_dev_16_25,Std_dev_32_25,Std_dev_64_25,Std_dev_128_25]

plt.figure()
plt.plot(x_MPI_processes, y_avg_time, '--', color='darkorange')
plt.errorbar(x_MPI_processes,y_avg_time, yerr=y_std_dev,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')
plt.xlabel('# of MPI processes')
plt.ylabel('mean time (s)')
plt.title('Ex 2 - Q2_5')
plt.grid()
plt.savefig('Ex2_Q2_5_plus128.png')


plt.figure()
y_avg_time_21=[Avg_time_8_21,Avg_time_16_21,Avg_time_32_21,Avg_time_64_21,Avg_time_128_21]
y_std_dev_21=[Std_dev_8_21,Std_dev_16_21,Std_dev_32_21,Std_dev_64_21,Std_dev_128_21]
y_avg_time_22=[Avg_time_8_22,Avg_time_16_22,Avg_time_32_22,Avg_time_64_22,Avg_time_128_22]
y_std_dev_22=[Std_dev_8_22,Std_dev_16_22,Std_dev_32_22,Std_dev_64_22,Std_dev_128_22]
y_avg_time_23=[Avg_time_8_23,Avg_time_16_23,Avg_time_32_23,Avg_time_64_23,Avg_time_128_23]
y_std_dev_23=[Std_dev_8_23,Std_dev_16_23,Std_dev_32_23,Std_dev_64_23,Std_dev_128_22]
y_avg_time_24=[Avg_time_8_24,Avg_time_16_24,Avg_time_32_24,Avg_time_64_24,Avg_time_128_24]
y_std_dev_24=[Std_dev_8_24,Std_dev_16_24,Std_dev_32_24,Std_dev_64_24,Std_dev_128_24]

plt.plot(x_MPI_processes, y_avg_time_21, '--', label='linear reduction')
plt.errorbar(x_MPI_processes,y_avg_time_21, yerr=y_std_dev_21,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.plot(x_MPI_processes, y_avg_time_22, '--', color='green',label='binary tree reduction')
plt.errorbar(x_MPI_processes,y_avg_time_22, yerr=y_std_dev_22,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.plot(x_MPI_processes, y_avg_time_23, '--', color='magenta',label='non-blocking - linear reduction')
plt.errorbar(x_MPI_processes,y_avg_time_23, yerr=y_std_dev_23,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.plot(x_MPI_processes, y_avg_time_24, '--', color='cyan',label='MPI Collective: MPI_Gather')
plt.errorbar(x_MPI_processes,y_avg_time_24, yerr=y_std_dev_24,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.plot(x_MPI_processes, y_avg_time, '--', color='darkorange', label='MPI Collective: MPI_Reduce')
plt.errorbar(x_MPI_processes,y_avg_time, yerr=y_std_dev,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')


plt.xlabel('# of MPI processes')
plt.ylabel('mean time (s)')
plt.title('Ex 2 - Q2_1 vs Q2_2 vs Q2_3 vs Q2_4 vs Q2_5')
plt.grid()
plt.legend()
plt.savefig('Ex2_Q2_1_VS_Q2_2_VS_Q2_3_VS_Q2_4_VS_Q2_5_plus128.png')
plt.show()
