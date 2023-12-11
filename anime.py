import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter([], [], c=[], cmap='viridis', s=100)

# Set plot limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)


# Update function for the animation
def update(frame):
    x = np.random.rand(10)
    y = np.random.rand(10)
    colors = np.random.rand(10)

    # Update scatter plot data
    scatter.set_offsets(np.column_stack((x, y)))
    scatter.set_array(colors)


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=200)

# Show the plot
plt.show()
