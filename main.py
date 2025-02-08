#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def pedal(x, a1, a2):
    y1 = a1 * x ** 2
    y2 = -a2 * x ** 2 + a1 + a2
    x_concat = np.concatenate([x, x[::-1]])
    y_concat = np.concatenate([y1, y2[::-1]])
    return x_concat, y_concat


if __name__ == '__main__':
    N = 1000
    a1 = 1.5
    a2 = 0.5

    x_orig = np.linspace(-1, 1, N)
    x_pedal, y_pedal = pedal(x_orig, a1, a2)

    plt.plot(x_pedal, y_pedal)
    plt.fill(x_pedal, y_pedal, color='pink', alpha=0.5)
    plt.axis('equal')
    plt.show()
