from tkinter import *
from tkinter import ttk

from frontend.tabs.Form import Form


"""

"""
class UI:
    def __init__(self, title, documentList):
        """

        """
        self._root = Tk()
        self._width = self._root.winfo_screenwidth()
        self._height = self._root.winfo_screenheight()
        self._root.title(title)
        self._root.geometry("%dx%d+0+0" % (self._width, self._height))
        self._notebook = ttk.Notebook(self._root)
        Form(self.__addTab('Documents'), documentList)
        self._root.mainloop()


    def __addTab(self, title):
        """

        """
        tab = ttk.Frame(self._notebook)
        self._notebook.add(tab, text=title)
        self._notebook.pack(expand=1, fill='both')
        return tab
