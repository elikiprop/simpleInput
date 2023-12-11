import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation




def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))

    line.set_data(x_data, y_data)
    return line,


# Setting up the figure and axis
fig, ax = plt.subplots()


x_data, y_data = [], []
line, = ax.plot([], [], lw=2)

# Setting the axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Code to create animation
animation = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100), blit=True)

# code to display the animation
plt.show()
