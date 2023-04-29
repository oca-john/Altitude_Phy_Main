import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
# Filter high frequency noise -> signal.filtfilt()


# Define filter function ===================================
def fltr (lins, ft_n):
    # lins2 = lins.iloc[:, 1]
    lins2 = lins[1]
    b, a = signal.butter(8, ft_n, 'low')
    ft_lins = signal.filtfilt(b, a, lins2)
    return ft_lins

# Import local data - Resp =================================
da = pd.read_csv('rsp_2resam.csv', index_col=0, parse_dates=True, header=None)
rspd = (da-da.min())/(da.max()-da.min())
# rspd = pd.read_csv("rsp_data.csv", header=None)
# ft_rspd = fltr(rspd, ft_n=0.03)
# rspd[2] = ft_rspd   # Writes temporary dataframe
ft_rspd2 = fltr(rspd, ft_n=0.035)
# rspd[3] = ft_rspd2
# ft_rspd3 = fltr(rspd, ft_n=0.04)
# rspd[4] = ft_rspd3
rspd[1] = ft_rspd2
rspd.to_csv("rsp_3filt.csv", header=False, index=True)

# Import local data - SPO ==================================
dc = pd.read_csv('spo_2resam.csv', index_col=0, parse_dates=True, header=None)
spod = (dc-dc.min())/(dc.max()-dc.min())
# spod = pd.read_csv("spo_data.csv", header=None)
# ft_spod = fltr(spod, ft_n=0.20)
# spod[2] = ft_spod
ft_spod2 = fltr(spod, ft_n=0.22)
# spod[3] = ft_spod2
# ft_spod3 = fltr(spod, ft_n=0.24)
# spod[4] = ft_spod3
spod[1] = ft_spod2
spod.to_csv("spo_3filt.csv", header=False, index=True)

# Plot =====================================================
# fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(8, 1, 
#     figsize=(24,10), sharex=True, sharey=False)
# ax1.plot(rspd[1], linewidth=0.8, alpha=0.6, label='rsp_data')
# ax1.legend()
# ax2.plot(rspd[2], linewidth=0.8, alpha=0.6, label='rsp_data 0.05')
# ax2.legend()
# ax3.plot(rspd[3], linewidth=0.8, alpha=0.6, label='rsp_data 0.1')
# ax3.legend()
# ax4.plot(rspd[4], linewidth=0.8, alpha=0.6, label='rsp_data 0.15')
# ax4.legend()
# ax5.plot(spod[1], linewidth=0.8, alpha=0.6, label='spo_data')
# ax5.legend()
# ax6.plot(spod[2], linewidth=0.8, alpha=0.6, label='spo_data 0.05')
# ax6.legend()
# ax7.plot(spod[3], linewidth=0.8, alpha=0.6, label='spo_data 0.1')
# ax7.legend()
# ax8.plot(spod[4], linewidth=0.8, alpha=0.6, label='spo_data 0.15')
# ax8.legend()
# plt.tight_layout()
# plt.show()
