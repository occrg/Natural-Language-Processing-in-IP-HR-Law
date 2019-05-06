from tkinter import *


"""

"""
class HeaderFrame:
    def __init__(self, master):
        """

        """
        self._master = master
        self._master.grid_columnconfigure(0, weight=20)
        self._master.grid_columnconfigure(1, weight=17)
        self._master.grid_columnconfigure(2, weight=7)
        self._master.grid_columnconfigure(3, weight=4)
        self._master.grid_columnconfigure(4, weight=18)
        self._master.grid_columnconfigure(5, weight=20)
        self._master.grid_rowconfigure(0, weight=1)


        self._titleLabel = Label(self._master, text="Title", font='Arial 14 bold')
        self._journalLabel = Label(self._master, text="Journal", font='Arial 14 bold')
        self._dateLabel = Label(self._master, text="Date", font='Arial 14 bold')
        self._testLabel = Label(self._master, text="Test", font='Arial 14 bold')
        self._pathLabel = Label(self._master, text="Path", font='Arial 14 bold')

        self._titleLabel.grid(row=0, column=0, sticky="s")
        self._journalLabel.grid(row=0, column=1, sticky="s")
        self._dateLabel.grid(row=0, column=2, sticky="s")
        self._testLabel.grid(row=0, column=3, sticky="s")
        self._pathLabel.grid(row=0, column=4, sticky="s")
