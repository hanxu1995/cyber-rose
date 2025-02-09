#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def pedal(a1, a2, c, N):
    x_max = np.sqrt(c / (a1 + a2))
    x = np.linspace(-x_max, x_max, N)
    y1 = a1 * x ** 2
    y2 = -a2 * x ** 2 + c
    x_concat = np.concatenate([x, x[::-1]])
    y_concat = np.concatenate([y1, y2[::-1]])
    return x_concat, y_concat


def rotate(x, y, theta):
    x_rotated = x * np.cos(theta) - y * np.sin(theta)
    y_rotated = x * np.sin(theta) + y * np.cos(theta)
    return x_rotated, y_rotated


def n_fold(x, y, n, turn=False):
    phi = 0 if not turn else np.pi / n
    result = [rotate(x, y, theta) for theta in np.linspace(0 + phi, 2 * np.pi + phi, n, endpoint=False)]
    return result


def stem(length, radius, num_points):
    z = np.linspace(0, -length, num_points)
    theta = np.linspace(0, 2 * np.pi, num_points)
    z, theta = np.meshgrid(z, theta)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y, z


def leaf(starting_z, a, b, phi, num_points):
    t = np.linspace(0, 2 * np.pi, num_points)
    x = a + a * np.cos(t)
    y = b * np.sin(t)
    z = starting_z + np.sqrt(x ** 2 + y ** 2) * np.cos(phi) / np.sin(phi)
    return x, y, z


if __name__ == '__main__':
    N = 1000
    num_pedals = 5
    num_layers = 5
    stem_height = 20
    stem_radius = 0.4
    a1s = np.linspace(1, 10, num_layers) / 4
    a2s = a1s / 3
    a3s = np.linspace(1, 10, num_layers) / 10
    cs = np.sqrt(10 / a3s) * np.linspace(1, 1.25, num_layers)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    colors = [
        (0.9, 0.4, 0.5),
        (0.8, 0.3, 0.4),
        (0.7, 0.2, 0.3),
        (0.6, 0.1, 0.2),
        (0.5, 0.0, 0.1)
    ]
    alphas = np.linspace(0.6, 0.9, num_layers)

    for j in range(num_layers):
        x_pedal, y_pedal = pedal(a1s[j], a2s[j], cs[j], N)
        result = n_fold(x_pedal, y_pedal, num_pedals, turn=j % 2 == 1)
        for i in range(num_pedals):
            z = a3s[j] * (result[i][0] ** 2 + result[i][1] ** 2)
            verts = [list(zip(result[i][0], result[i][1], z))]
            poly = Poly3DCollection(verts, facecolors=colors[j], alpha=alphas[j], edgecolor='gold', linewidths=1.5)
            ax.add_collection3d(poly)
    x_stem, y_stem, z_stem = stem(stem_height, stem_radius, N)
    ax.plot_surface(x_stem, y_stem, z_stem, color='green', alpha=0.8)

    # leaf
    x_leaf, y_leaf, z_leaf = leaf(-20 / 3, 3, 1.2, np.pi / 4, N)
    verts_leaf = [list(zip(x_leaf, y_leaf, z_leaf))]
    poly_leaf = Poly3DCollection(verts_leaf, facecolors='darkgreen', alpha=0.8, edgecolor='gold', linewidths=1.5)
    ax.add_collection3d(poly_leaf)

    ax.set_title("3D Flower")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-25, 20])
    ax.set_box_aspect([1, 1, 1])
    plt.axis('scaled')
    plt.show()
