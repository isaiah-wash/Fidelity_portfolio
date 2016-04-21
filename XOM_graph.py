import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import datetime
import matplotlib

XOM = pd.read_csv("XOM_yearexport.csv")

numpy_high = np.array(XOM.High)
numpy_open = np.array(XOM.Open)
numpy_close = np.array(XOM.Close)
numpy_low = np.array(XOM.Low)
numpy_date = np.array(XOM.Date)
datetime_dates= [ datetime.datetime.strptime(date, '%m/%d/%y') for date in numpy_date]

m, b = np.polyfit(matplotlib.dates.date2num(datetime_dates), numpy_open, 1)

print np.mean(numpy_open)




plt.plot_date(matplotlib.dates.date2num(datetime_dates), numpy_high, 'b-', label = 'High')
plt.plot_date(matplotlib.dates.date2num(datetime_dates), numpy_low, 'r-', label = 'Low')
plt.plot_date(matplotlib.dates.date2num(datetime_dates), numpy_open, 'g-', label = 'Open')
plt.plot(matplotlib.dates.date2num(datetime_dates), m*(matplotlib.dates.date2num(datetime_dates))+b, 'k-', label = 'LinReg')
plt.legend()
plt.title('ExXon Mobil Stock')
plt.ylabel('Price($)')

#XOM.plot(x="Date", y="Open")
#plt.hist(matplotlib.dates.date2num(datetime_dates), bins = 12)


plt.show()



