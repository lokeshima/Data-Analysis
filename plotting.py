import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

#workUnits=pd.read_csv('C:\Users\lokesh_chandra\PycharmProjects\Streaming\work_units.csv',header=None,names=['date_trunc','count'],index_col=0)
# #print(workUnits)
# #plot1=workUnits[1:3]
#
# print (workUnits)
#workUnits.set_index(workUnits['date_trunc'],inplace=True)
#workUnits.plot()
#plt.show()
#plt.plot(workUnits)

# read_csv = pd.read_csv('C:/Users/lokesh_chandra/PycharmProjects/Streaming/work_units.csv')
# read_csv['date_trunc'] = pd.to_datetime(read_csv['date_trunc'])
# #print(read_csv['count'])
# plt.plot(read_csv["date_trunc"], read_csv["count"])
#
# plt.show()
# #plt.clf()
#workUnits=pd.read_csv('C:\Users\lokesh_chandra\PycharmProjects\Streaming\work_units.csv',parse_dates=[1],infer_datetime_format=True,keep_date_col=True)
#workUnits= pd.DatetimeIndex(workUnits['Date'],format='%Y-%m-%d')

#plt.plot_date(x='Date', y='count', fmt="r-")
plt.plotfile('work_units.csv',(0,1))
plt.title("Workunits completed in a day")
plt.xlabel("Dates")
plt.ylabel("No. of Workunits")
#plt.grid(True)
plt.show()