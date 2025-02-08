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
    num_pedals = 5
    a1 = 1.5
    a2 = 0.5
    a3 = 1

    # x_orig = np.linspace(-1, 1, N)
    # x_pedal, y_pedal = pedal(x_orig, a1, a2)
    # result = n_fold(x_pedal, y_pedal, num_pedals)
    #
    # for i in range(num_pedals):
    #     plt.plot(result[i][0], result[i][1])
    #     plt.fill(result[i][0], result[i][1], color='pink', alpha=0.5)
    # plt.axis('equal')
    # plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)
    X, Y = np.meshgrid(x, y)
    Z = a3 * (X ** 2 + Y ** 2)
    Z[X ** 2 + Y ** 2 > 1] = np.nan

    ax.plot_surface(X, Y, Z, cmap='viridis')
    plt.axis('equal')
    plt.show()
