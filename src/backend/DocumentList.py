from backend.FilesIO import FilesIO
from backend.Document import Document
from backend.Classification import Classification
from backend.Visualisations import Visualisations


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


    def fillDocuments(self):
        self.__calculateDocumentFrequencies()
        self._classification = Classification(self)
        self._visualisations = Visualisations(self)

    def getDocuments(self):
        """

        """
        return self._documents


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
