from tkinter import *
from tkinter import ttk

from frontend.entry.HeaderFrame import HeaderFrame
from frontend.entry.EntryFrame import EntryFrame


"""

"""
class EntryHeaderFrame:
        """


        Arguments:
        master       ()
            --
        documentList ()
            --
        """
        self._master = master


        self._master.grid_rowconfigure(0, weight=1)
        self._master.grid_rowconfigure(1, weight=20)
        self._master.grid_columnconfigure(0, weight=1)


        self._headerFrame = Frame(self._master)
        self._headerFrame.grid(row=0, sticky="nsew")

        self._entryFrame = Frame(self._master)
        self._entryFrame.grid(row=1, sticky="nsew")

        self._headerObject = HeaderFrame(self._headerFrame)
        self._entryObject = EntryFrame(self._entryFrame, documentList)


    def getEntryObject(self):
        """
        Returns:
        self._entryObject ()
            -- 
        """
        return self._entryObject
