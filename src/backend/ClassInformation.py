from backend.FilesIO import FilesIO


"""

"""
class ClassInformation:

    io = FilesIO()

    def __init__(self, test, hrRat, ipRat, userRat, creatorRat, journal):
        """

        """
        self._gt = self.__deduceGt(journal)
        self._test = int(test)
        self._hrRat = float(hrRat)
        self._ipRat = float(ipRat)
        self._userRat = float(userRat)
        self._creatorRat = float(creatorRat)


    def getGt(self):
        """

        """
        return self._gt

    def setGt(self, gt):
        """

        """
        self._gt = gt


    def getHrRat(self):
        """

        """
        return self._hrRat

    def setHrRat(self, hrRat):
        """

        """
        self._hrRat = hrRat


    def getIpRat(self):
        """

        """
        return self._ipRat

    def setIpRat(self, ipRat):
        """

        """
        self._ipRat = ipRat


    def getUserRat(self):
        """

        """
        return self._userRat

    def setUserRat(self, userRat):
        """

        """
        self._userRat = userRat


    def getCreatorRat(self):
        """

        """
        return self._creatorRat

    def setCreatorRat(self, creatorRat):
        """

        """
        self._creatorRat = creatorRat


    def getTest(self):
        """

        """
        return self._test

    def setTest(self, test):
        """

        """
        self._test = test


    def __deduceGt(self, journal):
        """

        """
        if journal == "International Journal of Heritage Studies"            \
            or journal == "International Journal of Cultural Property"       \
            or journal == "Other: Human Rights":
            gt = 0
        elif journal == "Journal of Intellectual Property Law"               \
            or journal == "Journal of World Intellectual Property"           \
            or journal == "Other: Intellectual Property":
            gt = 1
        else:
            gt = "-"
        return gt
