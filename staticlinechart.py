import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)  
y = np.sin(x)                

plt.plot(x, y, color='blue', linewidth=2, label='sin(x)')


plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Static Line Chart Example")
plt.legend()

plt.show()
