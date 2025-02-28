#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# single 2d pedal
def pedal(a1, a2, c, num_points):
    x_max = np.sqrt(c / (a1 + a2))
    x = np.linspace(-x_max, x_max, num_points)
    y1 = a1 * x ** 2
    y2 = -a2 * x ** 2 + c
    x_concat = np.concatenate([x, x[::-1]])
    y_concat = np.concatenate([y1, y2[::-1]])
    return x_concat, y_concat


# rotate a 2d shape by theta
def rotate(x, y, theta):
    x_rotated = x * np.cos(theta) - y * np.sin(theta)
    y_rotated = x * np.sin(theta) + y * np.cos(theta)
    return x_rotated, y_rotated


# make n copies of a 2d shape and rotate them by (k/n)*2pi
# if turn=True, add phase phi=pi/n
def n_fold(x, y, n, turn=False):
    phi = 0 if not turn else np.pi / n
    result = [rotate(x, y, theta) for theta in np.linspace(0 + phi, 2 * np.pi + phi, n, endpoint=False)]
    return result


# a cylinder
def stem(length, radius, num_points):
    z = np.linspace(0, -length, num_points)
    theta = np.linspace(0, 2 * np.pi, num_points)
    z, theta = np.meshgrid(z, theta)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y, z


# an oval attached to the stem
def leaf(starting_z, a, b, phi, num_points):
    t = np.linspace(0, 2 * np.pi, num_points)
    x = a + a * np.cos(t)
    y = b * np.sin(t)
    z = starting_z + np.sqrt(x ** 2 + y ** 2) * np.cos(phi) / np.sin(phi)
    return x, y, z


if __name__ == '__main__':
    N = 1000  # number of points in each np.linspace
    num_pedals = 5  # number of pedals in a single layer
    num_layers = 5  # number of layers
    stem_length = 20  # length of stem
    stem_radius = 0.4  # radius of stem
    leaf_z = -20 / 3  # leaf location
    leaf_a = 3  # leaf half length
    leaf_b = 1.2  # leaf half width
    leaf_phi = np.pi / 4  # leaf angle
    a1s = np.linspace(1, 10, num_layers) / 4  # param for pedal lower part
    a2s = a1s / 3  # param for pedal upper part
    a3s = np.linspace(1, 10, num_layers) / 10  # param for layer
    cs = np.sqrt(10 / a3s) * np.linspace(1, 1.25, num_layers)  # param for pedal size

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    # rose-red colors
    colors = [
        (0.9, 0.4, 0.5),
        (0.8, 0.3, 0.4),
        (0.7, 0.2, 0.3),
        (0.6, 0.1, 0.2),
        (0.5, 0.0, 0.1)
    ]
    # opacity
    alphas = np.linspace(0.6, 0.9, num_layers)

    for j in range(num_layers):
        # for each layer
        # draw a 2d pedal
        x_pedal, y_pedal = pedal(a1s[j], a2s[j], cs[j], N)
        # draw n 2d pedals and rotate them
        result = n_fold(x_pedal, y_pedal, num_pedals, turn=j % 2 == 1)
        for i in range(num_pedals):
            # for each pedal
            # map the 2d pedal onto a 3d paraboloid
            z = a3s[j] * (result[i][0] ** 2 + result[i][1] ** 2)
            # add color and opacity for the 3d pedal
            verts = [list(zip(result[i][0], result[i][1], z))]
            poly = Poly3DCollection(verts, facecolors=colors[j], alpha=alphas[j], edgecolor='gold', linewidths=1.5)
            ax.add_collection3d(poly)
    # stem
    x_stem, y_stem, z_stem = stem(stem_length, stem_radius, N)
    ax.plot_surface(x_stem, y_stem, z_stem, color='green', alpha=0.8)

    # leaf
    x_leaf, y_leaf, z_leaf = leaf(leaf_z, leaf_a, leaf_b, leaf_phi, N)
    verts_leaf = [list(zip(x_leaf, y_leaf, z_leaf))]
    poly_leaf = Poly3DCollection(verts_leaf, facecolors='darkgreen', alpha=0.8, edgecolor='gold', linewidths=1.5)
    ax.add_collection3d(poly_leaf)

    # labels and axis
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
