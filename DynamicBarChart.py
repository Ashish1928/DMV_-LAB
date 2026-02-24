import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(1, 10, size=len(categories))

fig, ax = plt.subplots()
bars = ax.bar(categories, values, color='skyblue')
ax.set_ylim(0, 15)
ax.set_title("Dynamic Bar Chart")

def update(frame):
    new_values = np.random.randint(1, 15, size=len(categories))
    for bar, new_val in zip(bars, new_values):
        bar.set_height(new_val)
    return bars


ani = FuncAnimation(fig, update, frames=50, interval=500, blit=False)

plt.show()
