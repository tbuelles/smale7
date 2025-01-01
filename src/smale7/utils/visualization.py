from itertools import combinations
import numpy as np

def plot_sphere(ax):
    """Plots a sphere on the given 3D axis."""
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='c', alpha=0.1, edgecolor='k')

    # Set the axis limits
    ax.set_xlim([-0.75, 0.75])
    ax.set_ylim([-0.75, 0.75])
    ax.set_zlim([-0.75, 0.75])

    # Adjust the aspect ratio and remove additional margins
    ax.set_box_aspect([1, 1, 1])
    ax.axis('off')  # Turn off axis lines for a cleaner view

    # Adjust subplot position to remove margins
    ax.set_position([0.0, 0.0, 1.0, 1.0])


def plot_thomson(ax, points, N):
    """Plots the Thomson solution on a sphere."""
    plot_sphere(ax)
    for point in points:
        ax.scatter(*point, color='r', s=50)
    for i, j in combinations(range(N), 2):
        ax.plot(*zip(points[i], points[j]), color='b', alpha=0.5)