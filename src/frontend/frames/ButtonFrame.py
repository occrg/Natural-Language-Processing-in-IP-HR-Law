from tkinter import *
from tkinter import ttk


"""

"""
class ButtonFrame:
    def __init__(self, master):
        """

        """
        self._master = master

        self._master.grid_rowconfigure(0, weight=1)
        self._master.grid_rowconfigure(1, weight=1)
        self._master.grid_rowconfigure(2, weight=1)
        self._master.grid_columnconfigure(0, weight=1)


        addButton = Button(self._master, text="Add Document")
        testButton = Button(self._master, text="Change Test Data")
        trainButton = Button(self._master, text="Train Data")

        addButton.grid(row=1, column=1, padx=15, sticky = "nse")
        testButton.grid(row=1, column=2, padx=15, sticky = "nse")
        trainButton.grid(row=1, column=3, padx=15, sticky = "nse")