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

        self._canvas = FigureCanvasTkAgg(graph.getFig(), master=self._master)
        self._canvas.draw()
        self._canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        if graph.getTitle().startswith('3D'):
            graph.getAx().mouse_init()
        else:
            self._canvas.mpl_connect("button_press_event", lambda event, canvas=self._canvas : graph.hover(event, canvas))

        self._toolbar = NavigationToolbar2Tk(self._canvas, self._master)
        self._toolbar.update()
        self._canvas.mpl_connect("key_press_event", self.__on_key_press)


    def __on_key_press(self, event):
        """

        """
        key_press_handler(event, self._canvas, self._toolbar)
