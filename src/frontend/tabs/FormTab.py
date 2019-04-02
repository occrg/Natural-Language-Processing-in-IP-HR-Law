from tkinter import *
from tkinter import ttk

from frontend.frames.EntryHeaderFrame import EntryHeaderFrame
from frontend.frames.ButtonFrame import ButtonFrame


"""

"""
class FormTab:
    def __init__(self, master, uiObj, documentList):
        """

        """
        self._master = master

        self._master.grid_rowconfigure(0, weight=20)
        self._master.grid_rowconfigure(1, weight=1)
        self._master.grid_columnconfigure(0, weight=1)

        self._entryHeaderFrame = Frame(self._master, background="orange")
        self._entryHeaderFrame.grid(row=0, sticky="nesw")

        self._buttonFrame = Frame(self._master, background="green")
        self._buttonFrame.grid(row=1, sticky="nesw")

        EntryHeaderFrame(self._entryHeaderFrame, documentList)
        ButtonFrame(self._buttonFrame, uiObj, documentList)
