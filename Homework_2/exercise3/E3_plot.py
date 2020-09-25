import matplotlib.pyplot as plt
import numpy as np


# importing avg and std
x_stream_avg=[1,2,4,8,12,16,20,24,28,32]
y_stream_avg=np.loadtxt('summary_critical_avg.txt', unpack= True)
y_stream_std=np.loadtxt('summary_critical_std.txt', unpack= True)
yy_stream_avg=np.loadtxt('summary_noncrit_avg.txt', unpack= True)
yy_stream_std=np.loadtxt('summary_noncrit_std.txt', unpack= True)

plt.figure()
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

plt.figure()
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


'''
import pandas as pd

#df = pd.read_json('{"Schedules":{"0":"Static","1":"Dynamic","2":"Guided"},"count":{"0":83223.24,"1":225.74,"2":53504.3}}')
#df.plot(x='Schedules', y='count', kind='bar', legend=False)

df = pd.read_json('{"Schedules":{"0":"Static","1":"Dynamic","2":"Guided"},"count":{"0": 4.920 ,"1":2.353,"2":4.728}}')


df.plot(x='Schedules', y='count', kind='bar', legend=False)
plt.ylabel('Log')
plt.title('Ex 3 - Q1.3') 
plt.savefig('Ex2_Q1_3.png')
'''


plt.show()
import pdb
pdb.set_trace()
