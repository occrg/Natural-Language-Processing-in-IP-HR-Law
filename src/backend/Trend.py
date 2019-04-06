import statsmodels.api as sm
from scipy import stats
from sklearn import linear_model

import numpy as np

"""

"""
class Trend:
    def __init__(self, Xs, Ys):
        """

        """
        XsO = sm.add_constant(Xs)
        model = sm.RLM(Ys, XsO, M=sm.robust.norms.LeastSquares())
        results = model.fit()
        self._yintercept = results.params[0]
        self._gradient = results.params[1]
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
