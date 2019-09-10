from backend.FilesIO import FilesIO


"""
Stores the parent Document object's class related information.
"""
class ClassInformation:

    io = FilesIO()

    def __init__(self, test, hrRat, ipRat, userRat, creatorRat, journal):
        """
        Initialises a ClassInformation object.

        Arguments:
        test        (int)
            -- an integer representing whether the parent Document
               object is a test (1) or a train (0) document
        hrRat       (float)
            -- a float representing the human rights rating of the
               parent Document object
        ipRat       (float)
            -- a float representing the intellectual property rating of
               the parent Document object
        userRat     (float)
            -- a float representing the user rating of the parent
               Document object
        creatorRat  (float)
            -- a float representing the creator rating of the parent
               Document object

        Returns:
        journal     (str)
            -- a string representing the journal that the parent
               Document object comes from
        """
        self.deduceGt(journal)
        self._test = int(test)
        self._hrRat = float(hrRat)
        self._ipRat = float(ipRat)
        self._userRat = float(userRat)
        self._creatorRat = float(creatorRat)


    def getGt(self):
        """
        Returns:
        self._gt  (int)
            -- an integer representing the ground truth of the parent
               Document object either intellectual property (1) or
               human rights (0)
        """
        return self._gt

    def setGt(self, gt):
        """
        Arguments:
        self._gt  (int)
            -- an integer representing the ground truth of the parent
               Document object either intellectual property (1) or
               human rights (0)
        """
        self._gt = gt


    def getHrRat(self):
        """
        Returns:
        hrRat  (float)
            -- a float representing the human rights rating of the
               parent Document object
        """
        return self._hrRat

    def setHrRat(self, hrRat):
        """
        Arguments:
        hrRat  (float)
            -- a float representing the human rights rating of the
               parent Document object
        """
        self._hrRat = hrRat


    def getIpRat(self):
        """
        Returns:
        ipRat  (float)
            -- a float representing the intellectual property rating of
               the parent Document object
        """
        return self._ipRat

    def setIpRat(self, ipRat):
        """
        Arguments:
        ipRat  (float)
            -- a float representing the intellectual property rating of
               the parent Document object
        """
        self._ipRat = ipRat


    def getUserRat(self):
        """
        Returns:
        userRat  (float)
            -- a float representing the user rating of the parent
               Document object
        """
        return self._userRat

    def setUserRat(self, userRat):
        """
        Arguments:
        userRat  (float)
            -- a float representing the user rating of the parent
               Document object
        """
        self._userRat = userRat


    def getCreatorRat(self):
        """
        Returns:
        creatorRat  (float)
            -- a float representing the creator rating of the parent
               Document object
        """
        return self._creatorRat

    def setCreatorRat(self, creatorRat):
        """
        Arguments:
        creatorRat  (float)
            -- a float representing the creator rating of the parent
               Document object
        """
        self._creatorRat = creatorRat


    def getTest(self):
        """
        Returns:
        test  (int)
            -- an integer representing whether the parent Document
               object is a test (1) or a train (0) document
        """
        return self._test

    def setTest(self, test):
        """
        Arguments:
        test  (int)
            -- an integer representing whether the parent Document
               object is a test (1) or a train (0) document
        """
        self._test = test


    def deduceGt(self, journal):
        """
        Assigns the parent Document object's ground truth based on the
        journal it comes from

        Arguments:
        journal     (str)
            -- a string representing the journal that the parent
               Document object comes from
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
        self._gt = gt
