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


if __name__ == '__main__':
    N = 1000
    a1 = 1.5
    a2 = 0.5

    x_orig = np.linspace(-1, 1, N)
    x_pedal, y_pedal = pedal(x_orig, a1, a2)
    x_rotated, y_rotated = rotate(x_pedal, y_pedal, np.pi / 3)

    plt.plot(x_rotated, y_rotated)
    plt.fill(x_rotated, y_rotated, color='pink', alpha=0.5)
    plt.axis('equal')
    plt.show()
