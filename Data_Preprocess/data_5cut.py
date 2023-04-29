import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import signal
# Estimate the approximate stage (time boundary) from the 
# comparison of respiratory waveform of all subjects.
# Clipping and saving data by timestamp with a custom clipping function.
# Data is not used for plotting and presentation, so it is not flipped.


# Cut data function with return ============================
def cutd (lins_data, ta, tb):
    t1, t2 = [ta,tb]
    lins_rang = lins_data.loc[t1:t2]
    return lins_rang

# Read Source Data =========================================
da = pd.read_csv('rsp_3filt.csv', index_col=0, parse_dates=True, header=None)
da = (da-da.min())/(da.max()-da.min())
db = pd.read_csv('hr_1reorg.csv', index_col=0, parse_dates=True, header=None)
db = (db-db.min())/(db.max()-db.min())
dc = pd.read_csv('spo_3filt.csv', index_col=0, parse_dates=True, header=None)
dc = (dc-dc.min())/(dc.max()-dc.min())
dd = pd.read_csv('spv_1reorg.csv', index_col=0, parse_dates=True, header=None)
dd = (dd-dd.min())/(dd.max()-dd.min())
# dd = 1 - dd
de = pd.read_csv('prt_1reorg.csv', index_col=0, parse_dates=True, header=None)
de = (de-de.min())/(de.max()-de.min())

# Plot =====================================================
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9,4), sharex=True, sharey=True)
# # locator & formatter
# locator = mdates.AutoDateLocator(minticks=1, maxticks=30, interval_multiples=True)
# formatter = mdates.ConciseDateFormatter(locator)
# ax1.xaxis.set_major_locator(locator)
# ax1.xaxis.set_major_formatter(formatter)
# ax1.plot(da, linewidth=0.5, color='black', alpha=0.2, label='rsp_data')
# ax1.plot(db, linewidth=0.8, color='red', alpha=0.6, label='hr_data')
# ax1.plot(de, linewidth=0.8, color='blue', alpha=0.4, label='prt_data')
# # ax1.fill_between(x=de.index, y1=de[1], y2=0, color='green', alpha=0.1)
# ax1.tick_params(axis='y', labelsize=12)
# ax1.legend(loc='upper left', ncols=5, fancybox=True)
# ax2.plot(dc, linewidth=0.5, color='black', alpha=0.2, label='spo_data')
# ax2.plot(dd, linewidth=0.8, color='green', alpha=0.6, label='spv_data')
# ax2.plot(de, linewidth=0.8, color='blue', alpha=0.4, label='prt_data')
# ax2.tick_params(axis='x', labelsize=12)
# ax2.set_xlabel('Time(Min)',fontsize=12)
# ax2.tick_params(axis='y', labelsize=12)
# ax2.legend(loc='upper right', ncols=5, fancybox=True)
# plt.tight_layout()
# plt.show()

# Crop the data and save it ================================
# Define the target data range
glbta = '2023-02-17 09:14:51'
glbtb = '2023-02-17 09:56:00'
# Crop the data
dan = cutd(da, glbta, glbtb)
dan.to_csv('rsp_5cut.csv', header=False, index=True)
dbn = cutd(db, glbta, glbtb)
dbn.to_csv('hr_5cut.csv', header=False, index=True)
dcn = cutd(dc, glbta, glbtb)
dcn.to_csv('spo_5cut.csv', header=False, index=True)
ddn = cutd(dd, glbta, glbtb)
ddn.to_csv('spv_5cut.csv', header=False, index=True)
den = cutd(de, glbta, glbtb)
den.to_csv('prt_5cut.csv', header=False, index=True)
