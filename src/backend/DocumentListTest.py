from backend.FilesIO import FilesIO
from backend.Document import Document
from backend.Classification import Classification


"""

"""
class DocumentList:

    io = FilesIO()
    _dataFolder = 'data/'
    _detailsFile = _dataFolder + 'documentDetails0.csv'

    def __init__(self):
        """

        """
        self._documents = self.__processDocumentsFromRecords()
        self.calculateDocumentFrequencies()
        self._classification = Classification(self)
        # self.produceVisualisations()

    def getDocuments(self):
        """

        """
        return self._documents

    def calculateDocumentFrequencies(self):
        """

        """
        for document in self._documents:
            document.getCount().calculateFrequency(document.getFilename(), self.__getDocumentsWordLists())


    def produceVisualisations(self):
        """

        """
        pass


    def deduceAllWords(self):
        """

        """
        allWords = []
        for document in self._documents:
            words = document.getCount().getWords()
            for word in words:
                if word not in allWords:
                    allWords.append(word)


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
