import pandas as pd
import matplotlib.pyplot as plt 


# Read Source Data =========================================
# Note that the time cannot be resolved, or the timestamp becomes index
da = pd.read_csv('rsp_data.csv', header=None)
da2 = da.drop_duplicates()
da2.to_csv('rsp_1drop.csv', header=False, index=False)

dc = pd.read_csv('spo_data.csv', header=None)
dc2 = dc.drop_duplicates()
dc2.to_csv('spo_1drop.csv', header=False, index=False)

# Plot =====================================================
# plt.figure()
# plt.subplot(2,1,1)
# plt.plot(da[1], linewidth=0.5, color='black', alpha=0.2)
# plt.subplot(2,1,2)
# plt.plot(da2[1], linewidth=0.5, color='black', alpha=0.2)
# plt.show()
# print(len(da), len(da2))
