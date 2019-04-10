from tkinter import *
from tkinter import ttk


"""

"""
class ResultsTab:
    def __init__(self, master, documentList):
        """

        """
        self._master = master

        self._master.grid_columnconfigure(0, weight=1)
        self._master.grid_columnconfigure(1, weight=1)


        self._hripFrame = Frame(self._master, bg="grey", bd=10)
        self._hripFrame.grid(row=0, column=0, sticky="nesw")

        self._linesEvalFrame = Frame(self._master, bg="white", bd=10)
        self._linesEvalFrame.grid(row=0, column=1, sticky="nesw")

        self._hripTitle = Label(self._hripFrame, text="HR-IP Classification Evaluation", font='Times 18 bold', bg="white", justify=LEFT)
        self._hripTitle.grid(row=0, column=0, sticky = "nw")

        self._linesEvalTitle = Label(self._linesEvalFrame, text="Trend Line Evaluation", font='Times 18 bold', bg="white", justify=LEFT)
        self._linesEvalTitle.grid(row=0, column=0, sticky = "nw")

        try:
            documentList.getClassification()
            self._hripEval = Label(self._hripFrame, text="This is evaluation data", font='Times 14', bg="white", justify=LEFT)
            self._linesEval = Label(self._linesEvalFrame, text="This is evaluation data", font='Times 14', bg="white", justify=LEFT)
        except AttributeError as err:
            self._hripEval = Label(self._hripFrame, text="Please train model in document tab", font='Times 14', bg="white", justify=LEFT)
            self._linesEval = Label(self._linesEvalFrame, text="Please train model in document tab", font='Times 14', bg="white", justify=LEFT)

        self._hripEval.grid(row=1, column=0, sticky = "nw")
        self._linesEval.grid(row=1, column=0, sticky = "nw")
