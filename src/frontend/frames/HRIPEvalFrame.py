from tkinter import *
from tkinter import ttk

import statistics

from frontend.frames.HeaderFrame import HeaderFrame
from frontend.frames.EntryFrame import EntryFrame


"""

"""
class HRIPEvalFrame:
    def __init__(self, master, documentList):
        """

        """
        self._master = master


        self._title = Label(self._master, text="HR-IP Classification Evaluation", font='Times 18 bold', bg="white", justify=LEFT)
        self._title.grid(row=0, column=0, sticky = "nw")

        self._hripEval = []

        try:
            classification = documentList.getClassification()
            visualisations = documentList.getGraphs()

            self._hripEval.append(Label(self._master, text="Success ratio of graph shown: %f" % classification.getTestScore(), font='Times 14', bg="white", justify=LEFT, wraplength=940))
            self._hripEval.append(Label(self._master, text="Average success ratio across 5-fold cross validation: %f" % statistics.mean(classification.getCrossValScore()), font='Times 14', bg="white", justify=LEFT, wraplength=940))

            for c, label in enumerate(self._hripEval):
                label.grid(row=c+1, column=0, sticky="nw")


        except AttributeError as err:
            print(err)
            please = Label(self._master, text="Please train model in document tab", font='Times 14', bg="white", justify=LEFT)
            please.grid(row=1, column=0, sticky = "nw")
