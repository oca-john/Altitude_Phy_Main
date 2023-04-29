import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# Plot all signal stacks into two subplots and label them with key timestamps.


# Data
da = pd.read_csv('rsp_5cut.csv', index_col=0, parse_dates=True, header=None)
da = (da-da.min())/(da.max()-da.min())
db = pd.read_csv('hr_5cut.csv', index_col=0, parse_dates=True, header=None)
db = (db-db.min())/(db.max()-db.min())
dc = pd.read_csv('spo_5cut.csv', index_col=0, parse_dates=True, header=None)
dc = (dc-dc.min())/(dc.max()-dc.min())
dd = pd.read_csv('spv_5cut.csv', index_col=0, parse_dates=True, header=None)
dd = (dd-dd.min())/(dd.max()-dd.min())
dd2 = 1-dd
de = pd.read_csv('prt_5cut.csv', index_col=0, parse_dates=True, header=None)
de = (de-de.min())/(de.max()-de.min())
# de2 = 1-de

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,3), sharex=True, sharey=True)

# locator & formatter
locator = mdates.AutoDateLocator(minticks=1, maxticks=30, interval_multiples=True)
formatter = mdates.ConciseDateFormatter(locator)

ax1.xaxis.set_major_locator(locator)
ax1.xaxis.set_major_formatter(formatter)

ax1.plot(da, linewidth=0.08, color='black', alpha=0.2, label='rsp_data')
ax1.plot(db, linewidth=0.8, color='red', alpha=0.6, label='hr_data')
# ax1.plot(de, linewidth=0.8, color='blue', alpha=0.4, label='prt_data')
# ax1.fill_between(x=de.index, y1=de[1], y2=0, color='green', alpha=0.1)

ax1.vlines(datetime.strptime('2023-03-18 10:21:10.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='b', alpha=0.6)
ax1.text(datetime.strptime('2023-03-18 10:21:15.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.15, r'2.0 Km', fontsize=9)

ax1.vlines(datetime.strptime('2023-03-18 10:31:20.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='b', alpha=0.6)
ax1.text(datetime.strptime('2023-03-18 10:31:25.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.15, r'2.5 Km', fontsize=9)

ax1.vlines(datetime.strptime('2023-03-18 10:40:32.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='b', alpha=0.6)
ax1.text(datetime.strptime('2023-03-18 10:40:37.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.15, r'3.0 Km', fontsize=9)

ax1.vlines(datetime.strptime('2023-03-18 10:52:00.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='b', alpha=0.6)
ax1.text(datetime.strptime('2023-03-18 10:52:05.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.15, r'3.5 Km', fontsize=9)

ax1.vlines(datetime.strptime('2023-03-18 11:04:47.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='b', alpha=0.6)
ax1.text(datetime.strptime('2023-03-18 11:04:52.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.15, r'4.0 Km', fontsize=9)

ax1.tick_params(axis='y', labelsize=10)
ax1.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

ax2.plot(dc, linewidth=0.08, color='black', alpha=0.1, label='spo_data')
ax2.plot(dd2, linewidth=0.8, color='green', alpha=0.6, label='spv_data')
ax2.fill_between(x=dd2.index, y1=dd2[1], y2=1, color='green', alpha=0.1)
ax2.plot(de, linewidth=0.8, color='blue', alpha=0.4, label='prt_data')

ax2.vlines(datetime.strptime('2023-03-18 10:21:40.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='r', alpha=0.6)
ax2.text(datetime.strptime('2023-03-18 10:21:45.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.2, r'2.0 Km', fontsize=9)

ax2.vlines(datetime.strptime('2023-03-18 10:32:37.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='r', alpha=0.6)
ax2.text(datetime.strptime('2023-03-18 10:32:42.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.65, r'2.5 Km', fontsize=9)

ax2.vlines(datetime.strptime('2023-03-18 10:40:44.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='r', alpha=0.6)
ax2.text(datetime.strptime('2023-03-18 10:40:49.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.1, r'3.0 Km', fontsize=9)

ax2.vlines(datetime.strptime('2023-03-18 10:52:07.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='r', alpha=0.6)
ax2.text(datetime.strptime('2023-03-18 10:52:12.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.2, r'3.5 Km', fontsize=9)

ax2.vlines(datetime.strptime('2023-03-18 11:03:50.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0, 1, linewidth=1.2, colors='r', alpha=0.6)
ax2.text(datetime.strptime('2023-03-18 11:03:55.200', '%Y-%m-%d %H:%M:%S.%f'), 
            0.2, r'4.0 Km', fontsize=9)

ax2.tick_params(axis='x', labelsize=10)
ax2.set_xlabel('Time(Min)',fontsize=10)
ax2.tick_params(axis='y', labelsize=10)
ax2.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

plt.tight_layout()
plt.savefig('dplots.png')
plt.savefig('dplots.pdf')
plt.show()