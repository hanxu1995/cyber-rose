#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def pedal(x, a1, a2):
    y1 = a1 * x ** 2
    y2 = -a2 * x ** 2 + a1 + a2
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
    a1s = [1.0, 0.9, 0.8, 0.7, 0.6]
    a2 = 0.5
    a3s = [2, 3, 4, 5, 6]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    colors = plt.cm.viridis(np.linspace(0, 1, len(a3s)))

    x_orig = np.linspace(-1, 1, N)

    for j, a3 in enumerate(a3s):
        x_pedal, y_pedal = pedal(x_orig, a1s[j], a2)
        result = n_fold(x_pedal, y_pedal, num_pedals, turn=j % 2 == 1)
        for i in range(num_pedals):
            z = a3 * (result[i][0] ** 2 + result[i][1] ** 2)
            ax.plot3D(result[i][0], result[i][1], z, color=colors[j])

    ax.set_title("3D Layered Pedal Flower")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.view_init(elev=30, azim=45)
    plt.show()
