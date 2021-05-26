import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns
import pandas as pd

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]


'''Creating df'''
df = pd.DataFrame({"y1": [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
                   "y2": [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
                   "y3": [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
                   "y4": [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]})

'''calculate mean'''
mean = df.mean()
print("Mean:\n", mean)

'''calculate standard deviation'''
deviation = df.std()
print("Standard deviation:\n", deviation)

'''calculate correlation'''
correlation = df.corr()
print("Correlation:\n", correlation)

'''calculate variance'''
variance = df.var()
print("Variance:\n", variance)

'''show charts'''
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8, 8))
axs[0, 0].set(xlim=(0, 24), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24), yticks=(4, 6, 8, 10, 12, 14))

for ax, (label, (x, y)) in zip(axs.flat, datasets.items()):
    ax.plot(x, y, 'o')

    p1, p0 = np.polyfit(x, y, deg=1)
    ax.axline(xy1=(0, p0), slope=p1, color='b', lw=1)

plt.show()

try:
    os.mkdir("./anscombe")
except Exception:
    pass


fig.savefig('./anscombe/plot.png')


with open('./anscombe/result.csv', 'w', newline='') as file:
    calculate = csv.calculate(file)
    calculate.results(["Mean", "Deviation", "Variance"])
    for i, (m,d,v) in enumerate(zip(mean, deviation, variance)):
        calculate.results([m, d, v])
