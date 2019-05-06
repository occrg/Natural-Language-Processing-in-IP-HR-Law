from tkinter import *


"""

"""
class HRIPFrame:
    def __init__(self, master, documentList):
        """

        """
        self._master = master


        self._title = Label(self._master, text="HR-IP Classification Evaluation", font='Arial 18 bold', bg="white", justify=LEFT)
        self._title.grid(row=0, column=0, sticky = "nw")

        self._hripEval = []

        classification = documentList.getClassification()
        crossVal = documentList.getCrossValidation().getCrossValScore()
        tp, tn, fp, fn = classification.getTFPNs()

        self._hripEval.append(Label(self._master, text="Balanced accuracy of grpah classification: %f" % classification.getTestScore(), font='Arial 12', bg="white", justify=LEFT, wraplength=940))
        self._hripEval.append(Label(self._master, text="IP (Correct/Incorrect): (%d,%d)" % (tp, fn), font='Arial 12', bg="white", justify=LEFT, wraplength=940))
        self._hripEval.append(Label(self._master, text="HR (Correct/Incorrect): (%d,%d)" % (tn, fp), font='Arial 12', bg="white", justify=LEFT, wraplength=940))
        self._hripEval.append(Label(self._master, text="\nBalanced accuracy across 4-fold cross validation: %f, %.3f, %.3f, %.3f" % (crossVal[0], crossVal[1], crossVal[2], crossVal[3]), font='Arial 12', bg="white", justify=LEFT, wraplength=940))

        for c, label in enumerate(self._hripEval):
            label.grid(row=c+1, column=0, sticky="nw")
