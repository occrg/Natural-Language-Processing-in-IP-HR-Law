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


        self._title = Label(self._master, text="Trend Line Evaluation", font='Times 18 bold', bg="white", justify=LEFT)
        self._title.grid(row=0, column=0, sticky = "nw")

        self._linesEval = []

        try:
            classification = documentList.getClassification()
            graphs = documentList.getGraphs()

            r=1
            for graph in graphs:
                if not graph.getTitle().startswith('3D'):
                    trends = graph.getTrends()
                    independentVar = graph.getIndependentVar()
                    dependentVar = graph.getDependentVar()
                    for trend in trends:
                        pGradient = trend.getPgradient()
                        if trend.getGt():
                            category = "Intellectual Property"
                        else:
                            category = "Human Rights"
                        if trend.getGradient() > 0:
                            towards = "Intellectual Proprty"
                        else:
                            towards = "Human Rights"

                        if pGradient < trend.getStatSigLimit():
                            statsig = ""
                        else:
                            statsig = " not"
                        label = Label(self._master, text="%s documents %s trend towards %s over the %s.\nThis was found%s to be statistically significant with a p-value of %.3f" % (category, dependentVar, towards, dependentVar, statsig, pGradient), wraplength=940, font='Times 14', bg="white", justify=LEFT)
                        label.grid(row=r, column=0, sticky="nw")
                        self._linesEval.append(label)
                        r+=1
                    r+=1

        except AttributeError as err:
            print(err)
            please = Label(self._master, text="Please train model in document tab", font='Times 14', bg="white", justify=LEFT)
            please.grid(row=1, column=0, sticky = "nw")
