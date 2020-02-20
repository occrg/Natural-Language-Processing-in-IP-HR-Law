from tkinter import *
from tkinter import ttk

from frontend.entry.EntryHeaderFrame import EntryHeaderFrame
from frontend.entry.ButtonsFrame import ButtonsFrame


"""

"""
class EntryTab:
    def __init__(self, master, uiObj, documentList):
        """


        Arguments:
        master       ()
            --
        entryObj     ()
            --
        uiObj        ()
            --
        documentList (DocumentList)
            --
        """
        self._master = master

        self._master.grid_rowconfigure(0, weight=20)
        self._master.grid_rowconfigure(1, weight=1)
        self._master.grid_columnconfigure(0, weight=1)

        self._entryHeaderFrame = Frame(self._master)
        self._entryHeaderFrame.grid(row=0, sticky="nesw")

        self._buttonFrame = Frame(self._master)
        self._buttonFrame.grid(row=1, sticky="nesw")

        self._entryHeaderObject = EntryHeaderFrame(self._entryHeaderFrame, documentList)
        entryObj = self._entryHeaderObject.getEntryObject()
        self._buttonFooterObject = ButtonsFrame(self._buttonFrame, entryObj, uiObj, documentList)
