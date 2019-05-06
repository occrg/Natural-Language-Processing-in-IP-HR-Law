import random

from backend.FilesIO import FilesIO
from backend.Document import Document
from backend.Classification import Classification
from backend.Graph import Graph
from backend.Trend import Trend
from backend.CrossValidation import CrossValidation
from backend.TrendTools import TrendTools
from backend.UserCreatorRatingsCalc import UserCreatorRatingsCalc


"""

"""
class DocumentList:

    io = FilesIO()
    trendTools = TrendTools()
    ucCalc = UserCreatorRatingsCalc()


    def __init__(self):
        """

        """
        self._documents = []
        self._graphs = []
        self.__processDocumentsFromRecords()
        self.__calculateDocumentFrequencies()
        self.__compileAllFeatures()
        # self.__setRandomTestInstances(0.5) # TEMP
        self._classification = Classification()
        # self.generateClassifications() # TEMP
        self.ucCalc.userCreatorRatings(self._documents)
        self.trendAndVisualise()
        self._crossValidation = CrossValidation()
        # self._crossValidation.crossValidateAll(self, 4) # TEMP


    def trendAndVisualise(self):
        """

        """
        testDocuments = self.getTrainTestDocuments(1)
        date, hr_ip, user_creator =                                          \
            self.trendTools.arrangeIntoPoints(testDocuments)
        self._trends =                                                       \
            self.trendTools.generateTrends(date, hr_ip, user_creator)
        self.__generateVisualisations(date, hr_ip, user_creator)

    def generateClassifications(self):
        """

        """
        self._graphs = []
        self._classification.classifyDocuments(self)


    def __generateVisualisations(self, date, hr_ip, user_creator):
        """

        """
        noTrends = []
        iphrTrends = []
        usercreatorTrends = []
        iphrTrends.append(self._trends[0])
        iphrTrends.append(self._trends[1])
        usercreatorTrends.append(self._trends[2])
        usercreatorTrends.append(self._trends[3])
        graph3D = Graph('3D Graph', date, hr_ip, user_creator, noTrends, self)
        graphIPHR = Graph('IP-HR/Time', date, hr_ip, user_creator,           \
            iphrTrends, self)
        graphUserCreator = Graph('User-Creator/Time', date, hr_ip,           \
            user_creator, usercreatorTrends, self)
        graphIPHRUserCreator = Graph('User-Creator/IP-HR', date, hr_ip,      \
            user_creator, noTrends, self)


    def getDocuments(self):
        """

        """
        return self._documents

    def addDocument(self, document):
        """

        """
        self._documents.append(document)

    def removeDocument(self, document):
        """

        """
        self._documents.remove(document)

    def getGraphs(self):
        """

        """
        return self._graphs

    def addGraph(self, graph):
        """

        """
        self._graphs.append(graph)

    def getClassification(self):
        """

        """
        return self._classification

    def getTrends(self):
        """

        """
        return self._trends

    def getCrossValidation(self):
        """

        """
        return self._crossValidation

    def getAllFeatures(self):
        """

        """
        return self._allFeatures

    def getTrainTestDocuments(self, test):
        documents = []
        for document in self._documents:
            if document.getClassInformation().getTest() == test:
                documents.append(document)
        return documents

    def getGtDocuments(self, gt):
        documents = []
        for document in self._documents:
            if document.getClassInformation().getGt() == gt:
                documents.append(document)
        return documents


    def __calculateDocumentFrequencies(self):
        """

        """
        hrDocuments = self.getGtDocuments(0)
        ipDocuments = self.getGtDocuments(1)
        for document in self._documents:
            if document.getClassInformation().getGt():
                document.getCount().calculateTfidfCf(document.getFilename(), \
                    self.__getDocumentsWordLists(ipDocuments),               \
                    self.__getDocumentsWordLists(hrDocuments))
            else:
                document.getCount().calculateTfidfCf(document.getFilename(), \
                    self.__getDocumentsWordLists(hrDocuments),               \
                    self.__getDocumentsWordLists(ipDocuments))


    def __compileAllFeatures(self):
        """

        """
        self._allFeatures = []
        for document in self._documents:
            words = document.getCount().getFeatures()
            for word in words:
                if word not in self._allFeatures:
                    self._allFeatures.append(word)


    def __setRandomTestInstances(self, prop):
        total = len(self._documents)
        testNum = int(prop * total)
        trainNum = total - testNum
        ones = [1] * testNum
        zeros = [0] * trainNum
        listOfTests = []
        listOfTests.extend(ones)
        listOfTests.extend(zeros)
        random.shuffle(listOfTests)
        for c, document in enumerate(self._documents):
            document.getClassInformation().setTest(listOfTests[c])
            self.io.outputDocumentData(document)

    def __processDocumentsFromRecords(self):
        """

        """
        for line in self.io.getFileLinesAsList()[1:]:
            filename, title, journal, date, test, hrRat, ipRat, userRat,     \
                creatorRat = line.split(',')
            document = Document(filename, title, journal, date, test, hrRat, \
                ipRat, userRat, creatorRat)
            self._documents.append(document)


    def __getDocumentsWordLists(self, documents):
        """

        """
        wordLists = []
        for document in documents:
            wordLists.append(document.getCount().getFeatures())
        return wordLists
