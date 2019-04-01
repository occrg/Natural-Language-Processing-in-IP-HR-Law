from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

"""

"""
class Visualisation:
    def __init__(self, master):
        """

        """
        self._master = master


    def showFigures(self, visualisations):
        # for fig in figs:

        canvas = FigureCanvasTkAgg(visualisations.getFigs()[0], master=self._master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        visualisations.getAxs()[0].mouse_init()

        toolbar = NavigationToolbar2Tk(canvas, self._master)
        toolbar.update()
        canvas.mpl_connect("key_press_event", self.__on_key_press)

    def __on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
