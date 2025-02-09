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


if __name__ == '__main__':
    N = 1000
    num_pedals = 3
    num_layers = 5
    a1s = np.linspace(1, 10, num_layers) / 3
    a2s = a1s / 3
    a3s = np.linspace(1, 10, num_layers) / 3
    cs = np.sqrt(10 / a3s) * np.linspace(1, 1.25, num_layers)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = plt.cm.plasma(np.linspace(0, 1, num_layers))

    for j in range(num_layers):
        x_pedal, y_pedal = pedal(a1s[j], a2s[j], cs[j], N)
        result = n_fold(x_pedal, y_pedal, num_pedals, turn=j % 2 == 1)
        for i in range(num_pedals):
            z = a3s[j] * (result[i][0] ** 2 + result[i][1] ** 2)
            verts = [list(zip(result[i][0], result[i][1], z))]
            poly = Poly3DCollection(verts, facecolors=colors[j], alpha=0.8)
            ax.add_collection3d(poly)

    ax.set_title("3D Layered Pedal Flower")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    plt.show()
