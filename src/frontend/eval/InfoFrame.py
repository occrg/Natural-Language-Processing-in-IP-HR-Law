from tkinter import *

from frontend.eval.HRIPFrame import HRIPFrame
from frontend.eval.TrendsFrame import TrendsFrame


"""

"""
class InfoFrame:
    def __init__(self, master, documentList):
        """


        Arguments:
        master       ()
            --
        documentList ()
            --
        """
        self._master = master

        self._master.grid_columnconfigure(0, weight=1)
        self._master.grid_columnconfigure(1, weight=1)
        self._master.grid_rowconfigure(0, weight=1)

        self.__construct(documentList)


    def __construct(self, documentList):
        """


        Arguments:
        documentList ()
            --
        """
        self._hripFrame = Frame(self._master, bg="white", bd=10)
        self._hripFrame.grid(row=0, column=0, sticky="nesw")

        self._trendsFrame = Frame(self._master, bg="white", bd=10)
        self._trendsFrame.grid(row=0, column=1, sticky="nesw")

        self._hripObject = HRIPFrame(self._hripFrame, documentList)
        self._trendsObject = TrendsFrame(self._trendsFrame, documentList)


    def update(self, documentList):
        """


        Arguments:
        documentList ()
            --
        """
        self._hripFrame.destroy()
        self._trendsFrame.destroy()

        self.__construct(documentList)
