from tkinter import *
from tkinter import ttk

from frontend.frames.HeaderFrame import HeaderFrame
from frontend.frames.EntryFrame import EntryFrame


"""

"""
class EntryHeaderFrame:
    def __init__(self, master, documentList):
        """

        """
        self._master = master


        self._master.grid_rowconfigure(0, weight=1)
        self._master.grid_rowconfigure(1, weight=20)
        self._master.grid_columnconfigure(0, weight=1)


        self._headerFrame = Frame(self._master, background="pink")
        self._headerFrame.grid(row=0, sticky="nsew")

        self._entryFrame = Frame(self._master, background="red")
        self._entryFrame.grid(row=1, sticky="nsew")

        HeaderFrame(self._headerFrame)
        EntryFrame(self._entryFrame, documentList)
