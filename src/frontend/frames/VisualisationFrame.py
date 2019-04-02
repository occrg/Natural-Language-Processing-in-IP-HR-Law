from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


"""

"""
class VisualisationFrame:
    def __init__(self, master, graph):
        """

        """
        self._master = master

        canvas = FigureCanvasTkAgg(graph.getFig(), master=self._master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        if graph.getTitle().startswith('3D'):
            graph.getAx().mouse_init()

        toolbar = NavigationToolbar2Tk(canvas, self._master)
        toolbar.update()
        canvas.mpl_connect("key_press_event", self.__on_key_press)


    def __on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
