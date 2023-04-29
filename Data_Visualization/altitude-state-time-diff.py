import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Gradient changes in oxygen saturation and pulse rate at various altitudes. 
# Performance of blood oxygen and pulse rate at different altitudes and in 
# different states. The time difference between the respiratory and blood 
# oxygen waveforms in response to changes in the same altitude was counted 
# for all subjects.


# Data
dd1 = pd.read_csv('spv_6tag.csv', header=None, names=['Altitude levels (Km)', 'SpO2'])
de = pd.read_csv('prt_6tag.csv', header=None, names=['Altitude levels (Km)', 'Pulse rate'])

da1 = pd.read_csv('ps_p.csv', header=0, names=['Altitude range (Km)', 'Time shift (s)'])
db = pd.read_csv('ps_w.csv', header=0, names=['Altitude range (Km)', 'Time shift (s)'])
dc = pd.read_csv('pp_p.csv', header=0, names=['Altitude range (Km)', 'Time shift (s)'])
dd2 = pd.read_csv('pp_w.csv', header=0, names=['Altitude range (Km)', 'Time shift (s)'])

da2 = pd.read_csv('time_shift_fx.csv', header=0, names=['Altitude range (Km)', 'Time shift (s)'])


# Plot
sns.set(style='whitegrid', palette='muted', color_codes=True,font_scale=0.9,
        rc={'axes.edgecolor': 'black',
            'axes.linewidth': 0.9,
            'grid.color': 'gray',
            'grid.linestyle': 'dotted',})
fig = plt.figure(figsize=(8,4))

plt.subplot(2,3,1)
p1 = sns.boxenplot(data=dd1,x='Altitude levels (Km)', y='SpO2',width=0.6,
                linewidth=0.6,
                palette='pastel', scale='linear')
p1 = sns.stripplot(data=dd1,x='Altitude levels (Km)', y='SpO2',
                   alpha=0.12, marker='.', size=3, jitter=0.3, color="black")
p1.set(xlabel=None)


plt.subplot(2,3,(2,3))
p3 = sns.lineplot(data=da1, x='Altitude range (Km)', y='Time shift (s)', color="mediumblue",errorbar=('ci', 100),linestyle='dashed',lw=2,
                label='Platform period of SPO')
p3 = sns.lineplot(data=db, x='Altitude range (Km)', y='Time shift (s)', color="royalblue",errorbar=('ci', 100),linestyle='dotted',lw=2,
                label='Wave period of SPO')
p3 = sns.lineplot(data=dc, x='Altitude range (Km)', y='Time shift (s)', color="indianred",errorbar=('ci', 100),linestyle='dashed',lw=2,
                label='Platform period of Pulse Rate')
p3 = sns.lineplot(data=dd2, x='Altitude range (Km)', y='Time shift (s)', color="lightcoral",errorbar=('ci', 100),linestyle='dotted',lw=2,
                label='Wave period of Pulse Rate')
p3.set(xlabel=None)
p3.set(ylabel=None)
plt.legend(ncols=2, fancybox=True, fontsize=8)


plt.subplot(2,3,4)
p2 = sns.boxenplot(data=de,
                x='Altitude levels (Km)', y='Pulse rate', 
                width=0.6,
                linewidth=0.6,
                palette='pastel', scale='linear')
p2 = sns.stripplot(data=de,x='Altitude levels (Km)', y='Pulse rate', 
                alpha=0.12, marker='.', size=3, jitter=0.3, color="black")


plt.subplot(2,3,(5,6))
p4 = sns.scatterplot(data=da2,x='Altitude range (Km)', y='Time shift (s)', 
                alpha=0.4, marker='D', s=36, label='Time shift (s)',
                color="royalblue")
p4 = sns.regplot(data=da2, x='Altitude range (Km)', y='Time shift (s)', color="royalblue",order=2,scatter=False,
                line_kws={'linestyle':'-'})
p4.scatter(3.19, 0, c="firebrick")
plt.legend(ncols=2, fancybox=True, fontsize=8)


fig.text(0.03, 0.98, "a", size=14, rotation=0, ha="left", va="top", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.03, 0.48, "b", size=14, rotation=0, ha="left", va="bottom", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.36, 0.98, "c", size=14, rotation=0, ha="left", va="top", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))
fig.text(0.36, 0.48, "d", size=14, rotation=0, ha="left", va="bottom", bbox=dict(boxstyle="square", ec='white', fc='white', alpha=0.1))

plt.tight_layout()
plt.savefig('vis_comps3.png')
plt.savefig('vis_comps3.pdf')
plt.show()