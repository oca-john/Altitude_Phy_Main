import numpy as np
import pandas as pd
import scipy
from scipy import stats
import neurokit2 as nk
import matplotlib.pyplot as plt
# Autocorrelation of respiratory and oxygen saturation data, with respiratory 
# rate variability (RRV) and respiratory volume per time (RVT) calculated from 
# respiratory waveforms.


# Data
da = pd.read_csv('rsp_5cut.csv', index_col=0, parse_dates=True, header=None)
da = (da-da.min())/(da.max()-da.min())
dc = pd.read_csv('spo_5cut.csv', index_col=0, parse_dates=True, header=None)
dc = (dc-dc.min())/(dc.max()-dc.min())

# Plot
fig = plt.figure(figsize=(8,4))

plt.subplot(2,2,1)
signal = da[1]
n = len(signal)
signal = np.asarray(signal) - np.nanmean(signal)
a = np.concatenate((signal, np.zeros(n - 1)))  # added zeros
fft = np.fft.fft(a)
acf = np.fft.ifft(np.conjugate(fft) * fft)[:n]
acov = acf.real
# Normalize
r = acov / np.max(acov)
# Confidence interval
varacf = 1.0 / n
scipy.stats
interval = stats.norm.ppf(1 - 0.05 / 2.0) * np.sqrt(varacf)
ci_low, ci_high = r - interval, r + interval
plt.axhline(y=0, color="red", linestyle="--")
plt.plot(np.arange(0.01, len(r)/100 + 0.01, 0.01), r, 'r-', lw=0.6, alpha=0.6, label='RSP Autocorrelation (ACF)')
plt.ylabel("Autocorrelation r",fontsize=10)
plt.ylim(-0.1, 0.1)
plt.legend(loc='upper right', fontsize=8, ncols=5, fancybox=True)

plt.subplot(2,2,3)
signal = dc[1]
n = len(signal)
signal = np.asarray(signal) - np.nanmean(signal)
a = np.concatenate((signal, np.zeros(n - 1)))  # added zeros
fft = np.fft.fft(a)
acf = np.fft.ifft(np.conjugate(fft) * fft)[:n]
acov = acf.real
# Normalize
r = acov / np.max(acov)
# Confidence interval
varacf = 1.0 / n
scipy.stats
interval = stats.norm.ppf(1 - 0.05 / 2.0) * np.sqrt(varacf)
ci_low, ci_high = r - interval, r + interval
plt.axhline(y=0, color="blue", linestyle="--")
plt.plot(np.arange(0.01, len(r)/100 + 0.01, 0.01), r, 'b-', lw=0.6, alpha=0.6, label='SPO Autocorrelation (ACF)')
plt.ylabel("Autocorrelation r",fontsize=10)
plt.xlabel("Lag",fontsize=10)
plt.ylim(-0.1, 0.1)
plt.legend(loc='upper right', fontsize=8, ncols=5, fancybox=True)

plt.subplot(2,2,2)
lina = da[1]
signals, info = nk.rsp_process(lina, sampling_rate=100)
a = signals["RSP_Rate"]
plt.plot(np.arange(0,len(a)/100,0.01), a, 'r-', linewidth=0.6, alpha=0.6, label='Respiratory Rate Variability (RRV)')
plt.ylabel('Respiratory Rate',fontsize=10)
plt.legend(loc='upper left', fontsize=8, ncols=5, fancybox=True)

plt.subplot(2,2,4)
linb = da[1]
signals, info = nk.rsp_process(linb, sampling_rate=100)
a = signals["RSP_RVT"]
plt.plot(np.arange(0,len(a)/100,0.01), a, 'r-', linewidth=0.05, alpha=0.6, label='Respiratory Volume per Time (RVT)')
plt.fill_between(x=np.arange(0,len(a)/100,0.01), y1=a, y2=0, color='red', alpha=0.3)
plt.xlabel('Time (s)',fontsize=10)
plt.ylabel('Respiratory Volume',fontsize=10)
plt.legend(loc='upper left', fontsize=8, ncols=5, fancybox=True)

fig.text(0.03, 0.98, "a", size=14, rotation=0, ha="left", va="top", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.03, 0.48, "b", size=14, rotation=0, ha="left", va="bottom", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.56, 0.98, "c", size=14, rotation=0, ha="left", va="top", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.56, 0.48, "d", size=14, rotation=0, ha="left", va="bottom", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))

plt.tight_layout()
plt.savefig('vis_comps.png')
plt.savefig('vis_comps.pdf')
plt.show()