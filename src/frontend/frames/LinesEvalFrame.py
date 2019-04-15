from tkinter import *
from tkinter import ttk

from frontend.frames.HeaderFrame import HeaderFrame
from frontend.frames.EntryFrame import EntryFrame


"""

"""
class LinesEvalFrame:
    def __init__(self, master, documentList):
        """

        """
        self._master = master


        self._title = Label(self._master, text="Trend Line Evaluation", font='Arial 18 bold', bg="white", justify=LEFT)
        self._title.grid(row=0, column=0, sticky = "nw")

        self._linesEval = []

        try:
            classification = documentList.getClassification()
            graphs = documentList.getGraphs()

            r=0
            for graph in graphs:
                if not graph.getTitle().startswith('3D'):
                    trends = graph.getTrends()
                    independentVar = graph.getIndependentVar()
                    dependentVar = graph.getDependentVar()
                    for trend in trends:
                        grad = trend.getGradient()
                        pGradient = trend.getPgradient()
                        if trend.getGt():
                            category = "Intellectual Property"
                        else:
                            category = "Human Rights"
                        if grad > 0:
                            towards = trend.getHighCategory()
                        else:
                            towards = trend.getLowCategory()

                        r+=1
                        self._master.grid_rowconfigure(r, w=3)
                        if pGradient < trend.getStatSigLimit():
                            label = Label(self._master, text="%s documents %s trend towards %s over the %s with a slope of %f.\nThis was found to be statistically significant with a p-value of %.3f\n\n" % (category, dependentVar, towards, dependentVar, grad, pGradient), wraplength=940, font='Arial 12 bold', bg="white", justify=LEFT)
                        else:
                            label = Label(self._master, text="%s documents %s trend towards %s over the %s with a slope of %f.\nThis was found not to be statistically significant with a p-value of %.3f\n\n" % (category, dependentVar, towards, dependentVar, grad, pGradient), wraplength=940, font='Arial 12', bg="white", justify=LEFT)
                        label.grid(row=r, column=0, sticky="nw")
                        self._linesEval.append(label)
                    r+=1
                    self._master.grid_rowconfigure(r, w=1)

        except AttributeError as err:
            print(err)
            please = Label(self._master, text="Please train model in document tab", font='Arial 12s', bg="white", justify=LEFT)
            please.grid(row=1, column=0, sticky = "nw")
