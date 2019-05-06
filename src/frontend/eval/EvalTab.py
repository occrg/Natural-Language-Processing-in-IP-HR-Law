from tkinter import *

from frontend.eval.InfoFrame import InfoFrame
from frontend.eval.ButtonsFrame import ButtonsFrame


"""

"""
class EvalTab:
    def __init__(self, master, documentList):
        """

        """
        self._master = master

        self._master.grid_rowconfigure(0, weight=20)
        self._master.grid_rowconfigure(1, weight=1)
        self._master.grid_columnconfigure(0, weight=1)

        self._infoFrame = Frame(self._master)
        self._infoFrame.grid(row=0, sticky="nesw")

        self._buttonFrame = Frame(self._master)
        self._buttonFrame.grid(row=1, sticky="nesw")

        self._infoObject = InfoFrame(self._infoFrame, documentList)
        self._buttonObj =                                                    \
            ButtonsFrame(self._buttonFrame, documentList, self._infoObject)
