import pandas as pd
import neurokit2 as nk
import matplotlib.pyplot as plt
# Power spectrum and time-frequency spectrum of respiratory data and oxygen 
# saturation data.


# Data
da = pd.read_csv('rsp_5cut.csv', index_col=0, parse_dates=True, header=None)
da = (da-da.min())/(da.max()-da.min())
da = da[1]
db = pd.read_csv('spo_5cut.csv', index_col=0, parse_dates=True, header=None)
db = (db-db.min())/(db.max()-db.min())
db = db[1]

# Plot
fig = plt.figure(figsize=(8,4))

plt.subplot(2,2,1)
b = nk.signal_psd(da, method="lomb", min_frequency=1, max_frequency=20, show=False)
plt.plot(b.iloc[:,0], b.iloc[:,1], 'r-', linewidth=0.6, alpha=0.6, label='RSP Power (Lomb)')
plt.ylabel('Spectrum',fontsize=10)
plt.legend(loc='upper right',fontsize=10, ncols=5, fancybox=True)

plt.subplot(2,2,3)
c = nk.signal_psd(db, method="lomb", min_frequency=1, max_frequency=20, show=False)
plt.plot(c.iloc[:,0], c.iloc[:,1], 'b-', linewidth=0.6, alpha=0.6, label='SPO Power (Lomb)')
plt.xlabel('Frequency (Hz)',fontsize=10)
plt.ylabel('Spectrum',fontsize=10)
plt.legend(loc='upper right',fontsize=10, ncols=5, fancybox=True)

plt.subplot(2,2,2)
f1, t1, sig1 = nk.signal_timefrequency(da, 100, max_frequency=1, method='cwt',
                        show=False)
plt.pcolormesh(t1, f1, sig1, cmap='inferno')
plt.title('Continuous Wavelet Transform of RSP',fontsize=10)

plt.subplot(2,2,4)
f2, t2, sig2 = nk.signal_timefrequency(db, 100, max_frequency=1, method='cwt',
                        show=False)
plt.pcolormesh(t2, f2, sig2, cmap='inferno')
plt.xlabel('Time (sec)',fontsize=10)
plt.title('Continuous Wavelet Transform of SPO',fontsize=10)

fig.text(0.03, 0.98, "a", size=14, rotation=0, ha="left", va="top", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.03, 0.48, "b", size=14, rotation=0, ha="left", va="bottom", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.56, 0.98, "c", size=14, rotation=0, ha="left", va="top", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.56, 0.48, "d", size=14, rotation=0, ha="left", va="bottom", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))


plt.tight_layout()
plt.savefig('vis_comps2-1.jpg', dpi=300)
# plt.savefig('vis_comps2-1.pdf')
plt.show()