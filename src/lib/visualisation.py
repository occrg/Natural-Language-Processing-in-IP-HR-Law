import matplotlib.pyplot as plt
import numpy as np


def plot(Xs, Ys, Cs):
    """
    Plots the given data.

    Arguments:
    Xs  ([float]) -- the value of each sample document
    Ys  ([date])  -- the date that each sample document was created.
    Cs  ([str])   -- the colour that each set should be.
    """
    labels = ['hr', 'ip']
    for i in range(len(Xs)):
        plt.plot_date(Xs[i], Ys[i], fmt='o', c=Cs[i], label=labels[i])

    plt.legend()
    plt.axhline(y=0)
    plt.xticks(rotation=90)
    plt.ylim(-1,1)
    plt.show()
