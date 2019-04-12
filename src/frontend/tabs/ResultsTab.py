from tkinter import *
from tkinter import ttk

import statistics


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
            self._hripEval = Label(self._hripFrame, text="Success ratio of graph shown: %f" % documentList.getClassification().getTestScore(), font='Times 14', bg="white", justify=LEFT)
            self._hripEval.grid(row=1, column=0, sticky = "nw")

            self._hripEval1 = Label(self._hripFrame, text="Average success ratio across 5-fold cross validation: %f" % statistics.mean(documentList.getClassification().getCrossValScore()), font='Times 14', bg="white", justify=LEFT)
            self._hripEval1.grid(row=2, column=0, sticky = "nw")
            # 
            # self._linesEval = Label(self._linesEvalFrame, text="HR-IP/Time (HR) f-value: %f (with fp value: %f)" % (documentList.getGraphs()[1].getFvalue(), documentList.getGraphs()[1].getFpvalue()), font='Times 14', bg="white", justify=LEFT)
            # self._linesEval.grid(row=1, column=0, sticky = "nw")
            #
            # self._linesEval1 = Label(self._linesEvalFrame, text="This is evaluation data", font='Times 14', bg="white", justify=LEFT)
            # self._linesEval1.grid(row=2, column=0, sticky = "nw")
            #
            # self._linesEval2 = Label(self._linesEvalFrame, text="This is evaluation data", font='Times 14', bg="white", justify=LEFT)
            # self._linesEval2.grid(row=3, column=0, sticky = "nw")
            #
            # self._linesEval3 = Label(self._linesEvalFrame, text="This is evaluation data", font='Times 14', bg="white", justify=LEFT)
            # self._linesEval3.grid(row=4, column=0, sticky = "nw")
            #
            # self._linesEval4 = Label(self._linesEvalFrame, text="This is evaluation data", font='Times 14', bg="white", justify=LEFT)
            # self._linesEval4.grid(row=5, column=0, sticky = "nw")
            #
            # self._linesEval5 = Label(self._linesEvalFrame, text="This is evaluation data", font='Times 14', bg="white", justify=LEFT)
            # self._linesEval5.grid(row=6, column=0, sticky = "nw")
        except AttributeError as err:
            print(err)
            self._hripEval = Label(self._hripFrame, text="Please train model in document tab", font='Times 14', bg="white", justify=LEFT)
            self._hripEval.grid(row=1, column=0, sticky = "nw")

            self._linesEval = Label(self._linesEvalFrame, text="Please train model in document tab", font='Times 14', bg="white", justify=LEFT)
            self._linesEval.grid(row=1, column=0, sticky = "nw")
