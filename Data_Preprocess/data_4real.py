import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
# Remove baseline


# Read Source Data =========================================
# da = pd.read_csv('rsp_filt.csv', index_col=0, parse_dates=True, header=None)
# da = (da-da.min())/(da.max()-da.min())
dc = pd.read_csv('spo_3filt.csv', header=None)
dc2 = dc[1]
b, a = signal.butter(8, 0.02, 'low')
baseln = signal.filtfilt(b, a, dc2) # Baseline
dc_val = dc[1].values
dc_real = dc_val - baseln           # The flattened waveform
# print(baseln.shape, dc_val.shape, dc_real.shape)  # Check data shape
# fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(18,3), sharex=True)
# ax1.plot(dc_val, "b-", linewidth=0.2, alpha=0.5)
# ax2.plot(baseln, "b-", linewidth=0.2, alpha=0.5)
# ax3.plot(dc_real, "b-", linewidth=0.2, alpha=0.5)
# plt.tight_layout()
# plt.show()

# Save clean waveforms =====================================
spo_real = dc           # Share the type and index of the raw data
spo_real[1] = dc_real
spo_real.to_csv('spo_4real.csv', header=False, index=False)
