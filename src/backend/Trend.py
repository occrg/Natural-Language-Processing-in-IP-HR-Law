import statsmodels.api as sm
import numpy as np


"""

"""
class Trend:

    _statSigLimit = 0.05


    def __init__(self, gt, highCategory, lowCategory, independentVar,        \
        dependentVar, Xs, Ys):
        """


        Arguments:
        gt             (int)
            --
        highCategory   (string)
            --
        lowCategory    (string)
            --
        independentVar (string)
            --
        dependentVar   (string)
            --
        Xs             ([float])
            --
        Ys             ([float])
            --
        """
        self._gt = gt
        self._highCategory = highCategory
        self._lowCategory = lowCategory
        self._independentVar = independentVar
        self._dependentVar = dependentVar
        XsO = sm.add_constant(Xs)
        model = sm.OLS(Ys, XsO)
        results = model.fit()
        self._yintercept = results.params[0]
        self._gradient = results.params[1]
        self._pGradient = results.pvalues[1]
        self._x = np.linspace(min(Xs), max(Xs), 500)
        self._y = self._gradient * self._x + self._yintercept



    def getX(self):
        """
        Returns:
        self._x (np.)
            --
        """
        return self._x

    def getY(self):
        """
        Returns:
        self._y (float)
            --
        """
        return self._y

    def getGradient(self):
        """
        Returns:
        self._gradient (float)
            --
        """
        return self._gradient

    def getGt(self):
        """
        Returns:
        self._gt (int)
            --
        """
        return self._gt

    def getPgradient(self):
        """
        Returns:
        self._pGradient (float)
            --
        """
        return self._pGradient

    def getStatSigLimit(self):
        """
        Returns:
        self._statSigLimit (float)
            --
        """
        return self._statSigLimit

    def getHighCategory(self):
        """
        Returns:
        self._highCategory (string)
            --
        """
        return self._highCategory

    def getLowCategory(self):
        """
        Returns:
        self._lowCategory (string)
            --
        """
        return self._lowCategory

    def getIndependentVar(self):
        """
        Returns:
        self._independentVar (string)
            --
        """
        return self._independentVar

    def getDependentVar(self):
        """
        Returns:
        self._dependentVar (string)
            --
        """
        return self._dependentVar
