from tkinter import *
from tkinter import ttk

from frontend.frames.HRIPEvalFrame import HRIPEvalFrame
from frontend.frames.LinesEvalFrame import LinesEvalFrame


"""

"""
class ResultsTab:
    def __init__(self, master, documentList):
        """

        """
        self._master = master

        self._master.grid_columnconfigure(0, weight=1)
        self._master.grid_columnconfigure(1, weight=1)
        self._master.grid_rowconfigure(0, weight=1)

        self._hripEvalFrame = Frame(self._master, bg="white", bd=10)
        self._hripEvalFrame.grid(row=0, column=0, sticky="nesw")

        self._linesEvalFrame = Frame(self._master, bg="white", bd=10)
        self._linesEvalFrame.grid(row=0, column=1, sticky="nesw")

        self._hripEvalObject = HRIPEvalFrame(self._hripEvalFrame, documentList)
        self._linesEvalObject = LinesEvalFrame(self._linesEvalFrame, documentList)
