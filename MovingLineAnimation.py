import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_title("Moving Line Animation")
ax.set_xlim(0, 50)   
ax.set_ylim(-1, 1)  

x_data, y_data = [], []
(line,) = ax.plot([], [], lw=2, color="red")

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame * 0.2))  
   
    if len(x_data) > 50:
        x_data.pop(0)
        y_data.pop(0)
    
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=100, blit=True)

plt.show()
