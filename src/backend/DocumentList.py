from backend.FilesIO import FilesIO
from backend.Document import Document
from backend.Classification import Classification
from backend.Graph import Graph


"""

"""
class DocumentList:

    io = FilesIO()
    _dataFolder = 'data/'
    _detailsFile = _dataFolder + 'documentDetails-subset.csv'

    def __init__(self):
        """

        """
        self._documents = self.__processDocumentsFromRecords()
        self._graphs = []
        self.performVisualisations()


    def performClassifications(self):
        self._graphs = []
        self.__calculateDocumentFrequencies()
        self._classification = Classification(self)

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
        graphIPHRUserCreatpr = Graph('User-Creator/IP-HR', self)
        graphIPHRUserCreatpr.createIPHRUserCreatorGraph()
        self._graphs.append(graphIPHRUserCreatpr)

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

    def getTrainTestDocuments(self, test):
        documents = []
        for document in self._documents:
            if document.getClassInformation().getTest() == test:
                documents.append(document)
        return documents


    def __calculateDocumentFrequencies(self):
        """

        """
        for document in self._documents:
            document.getCount().calculateFrequency(document.getFilename(),   \
                self.__getDocumentsWordLists())


    def deduceAllWords(self):
        """

        """
        allWords = []
        for document in self._documents:
            words = document.getCount().getWords()
            for word in words:
                if word not in allWords:
                    allWords.append(word)
        return allWords


    def __processDocumentsFromRecords(self):
        """

        """
        documents = []
        for line in self.io.getFileLinesAsList()[1:]:
            filename, title, journal, date, test, hrRat, ipRat, userRat,     \
                creatorRat = line.split(',')
            document = Document(filename, title, journal, date, test, hrRat, \
                ipRat, userRat, creatorRat)
            documents.append(document)
        return documents


    def __getDocumentsWordLists(self):
        """

        """
        wordLists = []
        for document in self._documents:
            wordLists.append(document.getCount().getWords())
        return wordLists
