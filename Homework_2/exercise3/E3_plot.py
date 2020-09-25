import matplotlib.pyplot as plt
import numpy as np


# importing avg and std
x_stream_avg=[1,2,4,8,12,16,20,24,28,32]
y_stream_avg=np.loadtxt('summary_critical_avg.txt', unpack= True)
y_stream_std=np.loadtxt('summary_critical_std.txt', unpack= True)
yy_stream_avg=np.loadtxt('summary_noncrit_avg.txt', unpack= True)
yy_stream_std=np.loadtxt('summary_noncrit_std.txt', unpack= True)
yyy_stream_avg=np.loadtxt('summary_q4_avg.txt', unpack= True)
yyy_stream_std=np.loadtxt('summary_q4_std.txt', unpack= True)
yyyy_stream_avg=np.loadtxt('summary_padding_avg.txt', unpack= True)
yyyy_stream_std=np.loadtxt('summary_padding_std.txt', unpack= True)

plt.figure(1)
plt.hlines(0.001721, 1, 32, color='blueviolet', label ='serial')
plt.plot(x_stream_avg,y_stream_avg,'--', label='critical')
plt.errorbar(x_stream_avg, y_stream_avg, yerr=y_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.plot(x_stream_avg,yy_stream_avg,'--g', label='non critical')
plt.errorbar(x_stream_avg, yy_stream_avg, yerr=yy_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.xlabel('# of threads')
plt.ylabel('mean time (s)')
plt.title('Ex 3 - Q3_1')
plt.legend()
plt.grid()
plt.savefig('Ex3_Q3_1.png')

plt.figure(2)
plt.hlines(0.001721, 1, 32, color='blueviolet', label ='serial')
plt.semilogy(x_stream_avg,(y_stream_avg),'--', label='critical')
plt.errorbar(x_stream_avg, y_stream_avg, yerr=y_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.semilogy(x_stream_avg,yy_stream_avg,'--g', label='non critical')
plt.errorbar(x_stream_avg, yy_stream_avg, yerr=yy_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.xlabel('# of threads')
plt.ylabel('mean time (s)')
plt.title('Ex 3 - Q3_1 - semilogy')
plt.legend()
plt.grid()
plt.savefig('Ex3_Q3_1_semilogy.png')


plt.figure(3)
plt.hlines(0.001721, 1, 32, color='blueviolet', label ='serial')
plt.plot(x_stream_avg,yyy_stream_avg,'--',color='orange', label='local max')
plt.errorbar(x_stream_avg, yyy_stream_avg, yerr=yyy_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')
plt.xlabel('# of threads')
plt.ylabel('mean time (s)')
plt.title('Ex 3 - Q3_4')
plt.legend()
plt.grid()
plt.savefig('Ex3_Q3_4a.png')

plt.figure(4)
plt.hlines(0.001721, 1, 32, color='blueviolet', label ='serial')
plt.semilogy(x_stream_avg,(y_stream_avg),'--', label='critical')
plt.errorbar(x_stream_avg, y_stream_avg, yerr=y_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')
plt.plot(x_stream_avg,yyy_stream_avg,'--',color='orange', label='local max')
plt.errorbar(x_stream_avg, yyy_stream_avg, yerr=yyy_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.semilogy(x_stream_avg,yy_stream_avg,'--g', label='non critical')
plt.errorbar(x_stream_avg, yy_stream_avg, yerr=yy_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.xlabel('# of threads')
plt.ylabel('mean time (s)')
plt.title('Ex 3 - Q3_5 - semilogy')
plt.legend()
plt.grid()
plt.savefig('Ex3_Q3_4b.png')

plt.figure(5)
plt.hlines(0.001721, 1, 32, color='blueviolet', label ='serial')
plt.semilogy(x_stream_avg,(y_stream_avg),'--', label='critical')
plt.errorbar(x_stream_avg, y_stream_avg, yerr=y_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')
plt.plot(x_stream_avg,yyy_stream_avg,'--',color='orange', label='local max')
plt.errorbar(x_stream_avg, yyy_stream_avg, yerr=yyy_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.plot(x_stream_avg,yyyy_stream_avg,'--',color='black', label='padding')
plt.errorbar(x_stream_avg, yyyy_stream_avg, yerr=yyyy_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')


plt.semilogy(x_stream_avg,yy_stream_avg,'--g', label='non critical')
plt.errorbar(x_stream_avg, yy_stream_avg, yerr=yy_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')

plt.xlabel('# of threads')
plt.ylabel('mean time (s)')
plt.title('Ex 3 - Q3_5 - semilogy')
plt.legend()
plt.grid()
plt.savefig('Ex3_Q3_5.png')


plt.show()
import pdb
pdb.set_trace()
