import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
# Check the baseline of the signal


# Read Source Data =========================================
# da = pd.read_csv('rsp_filt.csv', index_col=0, parse_dates=True, header=None)
# da = (da-da.min())/(da.max()-da.min())
dc = pd.read_csv('spo_3filt.csv', header=None)
dc2 = dc[1]

# Filter parameter =========================================
# b, a = signal.butter(8, 0.01, 'low')
# ft_spod = signal.filtfilt(b, a, dc2)
# b, a = signal.butter(8, 0.02, 'low')
# ft_spod2 = signal.filtfilt(b, a, dc2)
# b, a = signal.butter(8, 0.03, 'low')
# ft_spod3 = signal.filtfilt(b, a, dc2)
# fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(18,8), sharex=True)
# ax1.plot(dc2, "b-", linewidth=0.2, alpha=0.5)
# ax2.plot(ft_spod, "r-", linewidth=0.2, alpha=0.5)
# ax3.plot(ft_spod2, "g-", linewidth=0.2, alpha=0.5)
# ax4.plot(ft_spod3, "b-", linewidth=0.2, alpha=0.5)
# plt.tight_layout()
# plt.show()

# Applied filter ===========================================
b, a = signal.butter(8, 0.02, 'low')
ft_spod2 = signal.filtfilt(b, a, dc2)   # baseline
# fig, (ax1) = plt.subplots(figsize=(18,3))
# ax1.plot(ft_spod2, "b-", linewidth=0.2, alpha=0.5)
# plt.tight_layout()
# plt.show()

# Save baseline ============================================
baseln = dc             # Share the type and index of the raw data
baseln[1] = ft_spod2
baseln.to_csv('spo_4baseln.csv', header=False, index=False)
