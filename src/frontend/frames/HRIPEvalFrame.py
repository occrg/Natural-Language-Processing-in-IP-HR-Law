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


        self._title = Label(self._master, text="HR-IP Classification Evaluation", font='Arial 18 bold', bg="white", justify=LEFT)
        self._title.grid(row=0, column=0, sticky = "nw")

        self._hripEval = []

        try:
            classification = documentList.getClassification()
            visualisations = documentList.getGraphs()
            tp, tn, fp, fn = classification.getTFPNs()
            crossVal = classification.getCrossValScore()

            self._hripEval.append(Label(self._master, text="Success ratio of graph shown: %f" % classification.getTestScore(), font='Arial 12', bg="white", justify=LEFT, wraplength=940))
            self._hripEval.append(Label(self._master, text="IP (Correct/Incorrect): (%d,%d)" % (tp, fn), font='Arial 12', bg="white", justify=LEFT, wraplength=940))
            self._hripEval.append(Label(self._master, text="HR (Correct/Incorrect): (%d,%d)" % (tn, fp), font='Arial 12', bg="white", justify=LEFT, wraplength=940))
            self._hripEval.append(Label(self._master, text="\nAverage success ratio across 4-fold cross validation: %.3f, %.3f, %.3f, %.3f" % (crossVal[0], crossVal[1], crossVal[2], crossVal[3]), font='Arial 12', bg="white", justify=LEFT, wraplength=940))

            for c, label in enumerate(self._hripEval):
                label.grid(row=c+1, column=0, sticky="nw")


        except AttributeError as err:
            print(err)
            please = Label(self._master, text="Please train model in document tab", font='Arial 12', bg="white", justify=LEFT)
            please.grid(row=1, column=0, sticky = "nw")
