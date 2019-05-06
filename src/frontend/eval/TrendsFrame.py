from tkinter import *

"""

"""
class TrendsFrame:
    def __init__(self, master, documentList):
        """

        """
        self._master = master


        self._title = Label(self._master, text="Trend Line Evaluation", font='Arial 18 bold', bg="white", justify=LEFT)
        self._title.grid(row=0, column=0, sticky = "nw")

        trendObjs = documentList.getTrends()
        trendsCrossVals = documentList.getCrossValidation().getTrendsCrossVal()

        for i in range(len(trendObjs)):
            trend = trendObjs[i]
            crossVal = trendsCrossVals[i]
            grad = trend.getGradient()
            pGradient = trend.getPgradient()

            independentVar = trend.getIndependentVar()
            dependentVar = trend.getDependentVar()

            if trend.getGt():
                category = "Intellectual Property"
            else:
                category = "Human Rights"

            if grad > 0:
                towards = trend.getHighCategory()
            else:
                towards = trend.getLowCategory()

            if pGradient < trend.getStatSigLimit():
                label = Label(self._master, text="%s documents' %s trend towards %s over the %s with a slope of %f.\nThis was found to be statistically significant with a p-value of %.4f" % (category, dependentVar, towards, independentVar, grad, pGradient), wraplength=940, font='Arial 12 bold', bg="white", justify=LEFT)
                crossValLabel = Label(self._master, text="p-values when in 4-fold cross-validation: %.4f, %.4f, %.4f, %.4f\n\n" % (crossVal[0], crossVal[1], crossVal[2], crossVal[3]), wraplength=940, font='Arial 12 bold', bg="white", justify=LEFT)
            else:
                label = Label(self._master, text="%s documents' %s trend towards %s over the %s with a slope of %f.\nThis was found not to be statistically significant with a p-value of %.4f" % (category, dependentVar, towards, independentVar, grad, pGradient), wraplength=940, font='Arial 12', bg="white", justify=LEFT)
                crossValLabel = Label(self._master, text="p-values when in 4-fold cross-validation: %.4f, %.4f, %.4f, %.4f\n\n" % (crossVal[0], crossVal[1], crossVal[2], crossVal[3]), wraplength=940, font='Arial 12', bg="white", justify=LEFT)

            label.grid(row=i*2 + 1, column=0, sticky="nw")
            crossValLabel.grid(row=i*2 + 2, column=0, sticky="nw")
