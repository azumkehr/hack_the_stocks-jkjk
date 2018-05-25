# Author: Andrew Zumkehr
# Purpose: Demonstrate pandas-datareader
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data, wb, DataReader
import backports.functools_lru_cache
from datetime import datetime
start = datetime(2018, 1, 1)
stop = datetime.now()

ibm = DataReader('IBM',  'yahoo', start, stop)
aapl= DataReader('AAPL',  'yahoo', start, stop)
print(ibm['Adj Close'])


print type(ibm)

print list(ibm.columns.values)

fig, ax1 = plt.subplots()
ax1.set_xlabel('Year')

ax1.set_ylabel('Close anomaly ($USD)', color = 'blue')
ax1.plot(ibm['Close']-np.mean(ibm['Close']), color = 'blue',label = 'IBM') 
ax1.plot(aapl['Close']-np.mean(aapl['Close']), color = 'red',label = 'Apple') 
ax1.tick_params(axis='y', color = 'black')


plt.legend()
plt.plot([start, stop],[0,0], color = 'black')
plt.title('IBM stock close')
plt.show()
