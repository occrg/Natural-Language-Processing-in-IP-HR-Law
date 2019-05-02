import statsmodels.api as sm
from scipy import stats
from sklearn import linear_model

import numpy as np

"""

"""
class Trend:

    _statSigLimit = 0.05


    def __init__(self, gt, highCategory, lowCategory, Xs, Ys):
        """

        """
        self._gt = gt
        self._highCategory = highCategory
        self._lowCategory = lowCategory
        XsO = sm.add_constant(Xs)
        model = sm.RLM(Ys, XsO, m=sm.robust.norms.LeastSquares)
        results = model.fit()
        self._yintercept = results.params[0]
        self._gradient = results.params[1]
        self._pGradient = results.pvalues[1]
        self._x = np.linspace(min(Xs), max(Xs), 500)
        self._y = self._gradient * self._x + self._yintercept



    def getX(self):
        """

        """
        return self._x

    def getY(self):
        """

        """
        return self._y

    def getGradient(self):
        """

        """
        return self._gradient

    def getGt(self):
        """

        """
        return self._gt

    def getPgradient(self):
        """

        """
        return self._pGradient

    def getStatSigLimit(self):
        """

        """
        return self._statSigLimit

    def getHighCategory(self):
        """

        """
        return self._highCategory

    def getLowCategory(self):
        """

        """
        return self._lowCategory
