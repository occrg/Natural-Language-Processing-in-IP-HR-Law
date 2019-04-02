from tkinter import *
from tkinter import ttk


"""

"""
class HeaderFrame:
    def __init__(self, master):
        """

        """
        self._master = master
        self._master.grid_columnconfigure(0, weight=3)
        self._master.grid_columnconfigure(1, weight=3)
        self._master.grid_columnconfigure(2, weight=2)
        self._master.grid_columnconfigure(3, weight=1)
        self._master.grid_columnconfigure(4, weight=4)
        self._master.grid_columnconfigure(5, weight=3)


        self._titleLabel = Label(self._master, text="Title")
        self._journalLabel = Label(self._master, text="Journal")
        self._dateLabel = Label(self._master, text="Date")
        self._testLabel = Label(self._master, text="Test")
        self._pathLabel = Label(self._master, text="Path")

        self._titleLabel.grid(row=0, column=0)
        self._journalLabel.grid(row=0, column=1)
        self._dateLabel.grid(row=0, column=2)
        self._testLabel.grid(row=0, column=3)
        self._pathLabel.grid(row=0, column=4)
