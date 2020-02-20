from backend.FilesIO import FilesIO


"""
Stores the parent Document's class related information.
"""
class ClassInformation:

    io = FilesIO()

    def __init__(self, test, hrRat, ipRat, userRat, creatorRat, journal):
        """
        Initialises a ClassInformation object.

        Arguments:
        test        (int)
            -- an integer representing whether the parent Document
               object is a test (1) or a training (0) document
        hrRat       (float)
            -- a rating of how much the document has language
               typical of the topic of human rights law
        ipRat       (float)
            -- a rating of how much the document has language
               typical of the topic of intellectual property law
        userRat     (float)
            -- a rating of how much the document has language
               suggesting the protection of the user of intellectual
               property
        creatorRat  (float)
            -- a rating of how much the document has language
               suggesting the protection of the creator of intellectual
               property
        journal     (str)
            -- the journal that the parent Document comes from
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
            -- a rating of how much the document has language
               typical of the topic of human rights law
        """
        return self._hrRat

    def setHrRat(self, hrRat):
        """
        Arguments:
        hrRat  (float)
            -- a rating of how much the document has language
               typical of the topic of human rights law
        """
        self._hrRat = hrRat


    def getIpRat(self):
        """
        Returns:
        ipRat  (float)
            -- a rating of how much the document has language
               typical of the topic of intellectual property law
        """
        return self._ipRat

    def setIpRat(self, ipRat):
        """
        Arguments:
        ipRat  (float)
            -- a rating of how much the document has language
               typical of the topic of intellectual property law
        """
        self._ipRat = ipRat


    def getUserRat(self):
        """
        Returns:
        userRat  (float)
            -- a rating of how much the document has language
               suggesting the protection of the user of intellectual
               property
        """
        return self._userRat

    def setUserRat(self, userRat):
        """
        Arguments:
        userRat  (float)
            -- a rating of how much the document has language
               suggesting the protection of the user of intellectual
               property
        """
        self._userRat = userRat


    def getCreatorRat(self):
        """
        Returns:
        creatorRat  (float)
            -- a rating of how much the document has language
               suggesting the protection of the creator of intellectual
               property
        """
        return self._creatorRat

    def setCreatorRat(self, creatorRat):
        """
        Arguments:
        creatorRat  (float)
            -- a rating of how much the document has language
               suggesting the protection of the creator of intellectual
               property
        """
        self._creatorRat = creatorRat


    def getTest(self):
        """
        Returns:
        test  (int)
            -- an integer representing whether the parent Document
               object is a test (1) or a training (0) document
        """
        return self._test

    def setTest(self, test):
        """
        Arguments:
        test  (int)
            -- an integer representing whether the parent Document
               object is a test (1) or a training (0) document
        """
        self._test = test


    def deduceGt(self, journal):
        """
        Assigns the parent Document's ground truth based on the journal
        it comes from

        Arguments:
        journal     (str)
            -- the journal that the parent Document comes from
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
