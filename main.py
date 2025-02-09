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
    a1 = 1
    a2 = 1 / 3
    c = 3.162
    theta = np.pi / 3

    x_pedal, y_pedal = pedal(a1, a2, c, N)
    x_rotated, y_rotated = rotate(x_pedal, y_pedal, theta)
    plt.plot(x_rotated, y_rotated)
    plt.fill(x_rotated, y_rotated, color='pink', alpha=0.5)

    plt.axis('scaled')
    plt.show()
