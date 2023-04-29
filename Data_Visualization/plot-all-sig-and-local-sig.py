import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
# Plot all signals separately and remove a small section of the 
# original respiratory and oxygen saturation waveforms to observe 
# their quality.


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
# Range Fill Function, Plot func with no return
# def frg (lins_data, axn, ta, tb):
#     t1, t2 = [ta,tb]
#     lins_rang = lins_data.loc[t1:t2]
#     axn.fill_between(x=lins_rang.index, y1=1, y2=0, color='red', alpha=0.1)

fig = plt.figure(figsize=(8,4))
gs1 = gridspec.GridSpec(nrows=10, ncols=4, hspace=0.1, 
                        top=0.99, bottom=0.01, left=0.02, right=0.99)
# locator & formatter
locator = mdates.AutoDateLocator(minticks=1, maxticks=30, interval_multiples=True)
formatter = mdates.ConciseDateFormatter(locator)

ax1 = fig.add_subplot(gs1[0:1, :-1])
ax1.xaxis.set_major_locator(locator)
ax1.xaxis.set_major_formatter(formatter)
ax1.plot(da, linewidth=0.2, color='black', alpha=0.3, label='rsp_data')
# frg(da, ax1, '2023-02-23 07:07:30','2023-02-23 07:07:57')
ax1.tick_params(axis='x', labelsize=9)
# for tick in ax1.xaxis.get_major_ticks():
#     tick.label.set_fontsize(6)
ax1.tick_params(axis='y', labelsize=9)
ax1.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

ax2 = fig.add_subplot(gs1[2:3, :-1], sharex=ax1)
ax2.plot(db, linewidth=0.8, color='red', alpha=0.6, label='hr_data')
ax2.tick_params(axis='x', labelsize=9)
ax2.tick_params(axis='y', labelsize=9)
ax2.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

ax3 = fig.add_subplot(gs1[4:5, :-1], sharex=ax1)
ax3.plot(dd2, linewidth=0.8, color='green', alpha=0.6, label='spv_data')
ax3.fill_between(x=dd2.index, y1=dd2[1], y2=1, color='green', alpha=0.1)
ax3.tick_params(axis='x', labelsize=9)
ax3.tick_params(axis='y', labelsize=9)
ax3.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

ax4 = fig.add_subplot(gs1[6:7, :-1], sharex=ax1)
ax4.plot(de, linewidth=0.8, color='blue', alpha=0.6, label='prt_data')
ax4.tick_params(axis='x', labelsize=9)
ax4.tick_params(axis='y', labelsize=9)
ax4.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

ax5 = fig.add_subplot(gs1[8:9, :-1], sharex=ax1)
ax5.plot(dc, linewidth=0.2, color='black', alpha=0.3, label='spo_data')
ax5.tick_params(axis='x', labelsize=9)
ax5.set_xlabel('Time(Min)',fontsize=10)
ax5.tick_params(axis='y', labelsize=9)
ax5.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

def picprt (lins_data, ta, tb):
    t1, t2 = [ta,tb]
    lins_range = lins_data.loc[t1:t2]
    return lins_range

ax6 = fig.add_subplot(gs1[0:4, -1])
dat6 = picprt(da, '2023-03-18 10:42:40','2023-03-18 10:43:00')
ax6.plot(dat6, linewidth=0.4, color='black', alpha=0.6, label='rsp_data')
ax6.tick_params(axis='y', labelsize=9)
ax6.tick_params(axis='x', labelsize=8, rotation=30)
ax6.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

ax7 = fig.add_subplot(gs1[5:9, -1], sharex=ax6)
dat7 = picprt(dc, '2023-03-18 10:42:40','2023-03-18 10:43:00')
ax7.plot(dat7, linewidth=0.4, color='black', alpha=0.6, label='spo_data')
ax7.tick_params(axis='y', labelsize=9)
ax7.tick_params(axis='x', labelsize=8, rotation=30)
ax7.legend(loc='upper left', fontsize=9, ncols=5, fancybox=True)

fig.text(0.02, 0.02, "a", size=12, rotation=0, ha="left", va="bottom",
         bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.98, 0.98, "b", size=12, rotation=0, ha="right", va="top",
         bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.98, 0.48, "c", size=12, rotation=0, ha="right", va="top",
         bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))

plt.savefig('dplots-div.png')
plt.savefig('dplots-div.pdf')
plt.show()