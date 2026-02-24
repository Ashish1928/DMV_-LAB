import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_title("Dynamic Histogram")
ax.set_xlim(0, 10)  
ax.set_ylim(0, 50)  

data = np.random.randn(1000)

counts, bins, patches = ax.hist(data, bins=20, color='skyblue', edgecolor='black')

def update(frame):
    ax.cla() 
    ax.set_title("Dynamic Histogram")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 50)
    
    new_data = np.random.uniform(0, 10, 1000)
    ax.hist(new_data, bins=20, color='orange', edgecolor='black')

ani = FuncAnimation(fig, update, frames=50, interval=500, blit=False)

plt.show()
