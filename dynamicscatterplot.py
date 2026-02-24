import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


n_points = 20


x = np.random.rand(n_points)
y = np.random.rand(n_points)

fig, ax = plt.subplots()
sc = ax.scatter(x, y, c='blue', s=50)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Dynamic Scatter Plot")


def update(frame):
   
    x = np.random.rand(n_points)
    y = np.random.rand(n_points)
    sc.set_offsets(np.c_[x, y])
    ax.set_title(f"Dynamic Scatter Plot - Frame {frame}")


ani = FuncAnimation(fig, update, frames=30, interval=500, repeat=False)

plt.show()
