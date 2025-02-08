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


def n_fold(x, y, n):
    result = [rotate(x, y, theta) for theta in np.linspace(0, 2 * np.pi, n, endpoint=False)]
    return result


if __name__ == '__main__':
    N = 1000
    num_pedals = 3
    a1 = 0.8
    a2 = 0.5
    a3 = 1

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_orig = np.linspace(-1, 1, N)
    x_pedal, y_pedal = pedal(x_orig, a1, a2)
    result = n_fold(x_pedal, y_pedal, num_pedals)

    for i in range(num_pedals):
        z = a3 * (result[i][0] ** 2 + result[i][1] ** 2)
        ax.plot3D(result[i][0], result[i][1], z, color='purple')
    plt.axis('equal')
    plt.show()
