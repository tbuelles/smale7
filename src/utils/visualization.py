from itertools import combinations
import numpy as np

def plot_sphere(ax):
    """Plots a sphere on the given 3D axis."""
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='c', alpha=0.2, edgecolor='k')

def plot_thomson(points, ax, N):
    """Plots the Thomson solution on a sphere."""
    plot_sphere(ax)
    for point in points:
        ax.scatter(*point, color='r', s=50)
    for i, j in combinations(range(N), 2):
        ax.plot(*zip(points[i], points[j]), color='b', alpha=0.6)
    ax.set_title(f"N = {N}")
    ax.set_box_aspect([1, 1, 1])
    ax.axis('off')