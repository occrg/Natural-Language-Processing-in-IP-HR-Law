from tkinter import *
from tkinter import ttk

from frontend.entry.EntryTab import EntryTab
from frontend.visualisation.VisualisationTab import VisualisationTab
from frontend.eval.EvalTab import EvalTab


"""

"""
class UI:
    def __init__(self, title, documentList):
        """


        Arguments:
        title        ()
            --
        documentList ()
            --
        """
        self._root = Tk()
        self._width = self._root.winfo_screenwidth()
        self._height = self._root.winfo_screenheight()
        self._root.title(title)
        self._root.geometry("%dx%d+0+0" % (self._width, self._height))
        self._notebook = ttk.Notebook(self._root)
        self._visualisationObj = VisualisationTab(self.addTab('Visualisations'), documentList.getGraphs())
        self._resultsObj = EvalTab(self.addTab('Results'), documentList)
        self._formObj = EntryTab(self.addTab('Documents'), self, documentList)
        self._root.mainloop()


    def addTab(self, title):
        """


        Arguments:
        title (string)
            --

        Returns:
        tab (ttk.Frame)
            --
        """
        tab = ttk.Frame(self._notebook)
        self._notebook.add(tab, text=title)
        self._notebook.pack(expand=1, fill='both')
        return tab

    def insertTab(self, place, title):
        """


        Arguments:
        place (int)
            --

        title (string)
            --

        Returns:
        tab (ttk.Frame)
            --
        """
        tab = ttk.Frame(self._notebook)
        self._notebook.insert(place, tab, text=title)
        self._notebook.pack(expand=1, fill='both')
        return tab

    def getNotebook(self):
        """
        Returns:
        self._notebook (ttk.Notebook)
            -- 
        """
        return self._notebook
