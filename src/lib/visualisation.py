import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plot(Xs, Ys, Zs, Cs):
    """
    Plots the given data.

    Arguments:
    Xs  ([float]) -- the value of each sample document
    Ys  ([date])  -- the date that each sample document was created.
    Cs  ([str])   -- the colour that each set should be.
    """
    ZsScale = [(x - 0.06) * 9 for x in Zs]
    fig = plt.figure()
    ax = Axes3D(fig)
    labels = ['Human Rights', 'Intellectual Property']
    for i in range(len(Xs)):
        ax.scatter(Xs[i], Ys[i], ZsScale[i], s=40, marker='o', c=Cs[i], label=labels[i])

    plt.legend()
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_xlabel("Time", fontsize='large', fontweight='bold')
    ax.set_ylabel("HR-IP scale", fontsize='large', fontweight='bold')
    ax.set_zlabel("Creator-User scale", fontsize='large', fontweight='bold')
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    yearsFmt = mdates.DateFormatter('%Y')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)
    ax.tick_params(axis='x', labelrotation=90, which='major', pad=0)
    ax.tick_params(axis='y', labelrotation=45, which='major', pad=0)
    ax.tick_params(axis='z', labelrotation=45, which='major', pad=0)
    ax.xaxis.labelpad = 23
    ax.yaxis.labelpad = 18
    ax.zaxis.labelpad = 4
    ax.xaxis.label.set_color([0,0.733,0.839])
    ax.yaxis.label.set_color([0,0.733,0.839])
    ax.zaxis.label.set_color([0,0.733,0.839])
    plt.ylim(-1,1)
    plt.show()
