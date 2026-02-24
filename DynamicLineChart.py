import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_title("Dynamic Line Chart")
ax.set_xlim(0, 100)   
ax.set_ylim(-1, 1)   

x_data, y_data = [], []
(line,) = ax.plot([], [], lw=2, color="blue")

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame * 0.1)) 
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100, blit=True)

plt.show()
