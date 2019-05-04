import random

from backend.FilesIO import FilesIO
from backend.Document import Document
from backend.Classification import Classification
from backend.Graph import Graph


"""

"""
class DocumentList:

    io = FilesIO()


    def __init__(self):
        """

        """
        self._documents = []
        self.__processDocumentsFromRecords()
        self.calculateDocumentFrequencies() # TEMP
        self._graphs = []
        self._classification = Classification()
        self.performVisualisations()


    def performClassifications(self):
        self._graphs = []
        self._classification.classifyDocuments(self)

    def performVisualisations(self):
        graph3D = Graph('3D Graph', self)
        graph3D.create3dGraph()
        self._graphs.append(graph3D)
        graphIPHR = Graph('IP-HR/Time', self)
        graphIPHR.createIPHRgraph()
        self._graphs.append(graphIPHR)
        graphUserCreator = Graph('User-Creator/Time', self)
        graphUserCreator.createUserCreatorGraph()
        self._graphs.append(graphUserCreator)
        graphIPHRUserCreator = Graph('User-Creator/IP-HR', self)
        graphIPHRUserCreator.createIPHRUserCreatorGraph()
        self._graphs.append(graphIPHRUserCreator)

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

    def getClassification(self):
        """

        """
        return self._classification

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


    def calculateDocumentFrequencies(self):
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


    def compileAllFeatures(self):
        """

        """
        self._allFeatures = []
        for document in self._documents:
            words = document.getCount().getFeatures()
            for word in words:
                if word not in self._allFeatures:
                    self._allFeatures.append(word)


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
