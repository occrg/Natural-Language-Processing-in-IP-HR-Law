from tkinter import *

from frontend.visualisation.VisualisationFrame import VisualisationFrame


"""

"""
class VisualisationTab:
    def __init__(self, master, graphs):
        """

        """
        self._master = master
        self._tabs = []
        self._objs = []
        self._notebook = ttk.Notebook(self._master)
        for graph in graphs:
            tab = self.__addTab(graph.getTitle())
            self._tabs.append(tab)
            self._objs.append(VisualisationFrame(tab, graph))


    def __addTab(self, title):
        """

        """
        tab = ttk.Frame(self._notebook)
        self._notebook.add(tab, text=title)
        self._notebook.pack(expand=1, fill='both')
        return tab
