import matplotlib.pyplot as plt
import numpy as np


# importing avg and std
x_stream_avg=[1,2,4,8,12,16,20,24,28,32]
y_stream_avg=np.loadtxt('summary_avg.txt', unpack= True)
y_stream_std=np.loadtxt('summary_std.txt', unpack= True)



plt.plot(x_stream_avg,y_stream_avg,'--')
plt.errorbar(x_stream_avg, y_stream_avg, yerr=y_stream_std,fmt='rs',capsize=5,markersize=3,elinewidth=2,ecolor='k')
plt.xlabel('# of threads')
plt.ylabel('copy bandwidth [MB/s]')
plt.title('Ex 2 - Q1.1')
plt.grid()
#plt.savefig('Ex2_Q1_1.png')



import pandas as pd

#df = pd.read_json('{"Schedules":{"0":"Static","1":"Dynamic","2":"Guided"},"count":{"0":83223.24,"1":225.74,"2":53504.3}}')
#df.plot(x='Schedules', y='count', kind='bar', legend=False)

df = pd.read_json('{"Schedules":{"0":"Static","1":"Dynamic","2":"Guided"},"count":{"0": 4.920 ,"1":2.353,"2":4.728}}')


df.plot(x='Schedules', y='count', kind='bar', legend=False)
plt.ylabel('Log')
plt.title('Ex 2 - Q1.3') 
plt.savefig('Ex2_Q1_3.png')
plt.show()
import pdb
pdb.set_trace()
