import pandas as pd
import matplotlib.pyplot as plt
# Resampled data at 100 data per second.

# Read Source Data =========================================
da = pd.read_csv('rsp_1reorg.csv', index_col=0, parse_dates=True, header=None)
dc = pd.read_csv('spo_1reorg.csv', index_col=0, parse_dates=True, header=None)

# Resample =================================================
da1 = da.resample('10L').mean()
da2 = da1.interpolate(method='linear')  # Original signal
# da2 = da1.interpolate(method='polynomial', order=2)  # smoother
da2.to_csv('rsp_2resam.csv', header=False, index=True)

dc1 = dc.resample('10L').mean()
dc2 = dc1.interpolate(method='linear')
dc2.to_csv('spo_2resam.csv', header=False, index=True)

# Plot =====================================================
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(19,6), sharex=True)
# ax1.plot(da, linewidth=0.5, color='blue', alpha=0.2)
# ax2.plot(da2, linewidth=0.5, color='red', alpha=0.2)
# plt.tight_layout()
# plt.show()
# print(len(da), len(da2))
