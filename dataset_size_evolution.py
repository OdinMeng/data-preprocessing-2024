import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

nums = [10008, 9867, 9724, 9724, 9719, 9610, 9599, 9191, 8579]
R = np.arange(len(nums))

ax.plot(R, nums, marker='o')

trans = ax.get_xaxis_transform()


ax.axvline(x=1, color='r', linestyle='--', alpha=.75)
plt.text(1.05, 0.05, 'Outliers Removal', transform=trans, color='darkred')

ax.axvline(x=7, color='r', linestyle='--', alpha=.75)
plt.text(4.3, 0.05, 'Inconsistency Checks', transform=trans, color='darkred')

ax.axvline(x=8, color='r', linestyle='--', alpha=.75)
plt.text(6.15, 0.95, 'ID Consistency', transform=trans, color='darkred')

plt.tick_params(    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off)

fig.suptitle("Dataset Size Evolution")

plt.show()