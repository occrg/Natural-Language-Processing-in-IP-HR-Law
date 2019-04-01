from backend.FilesIO import FilesIO
from backend.PDFtext import PDFtext
from backend.PDFmetadata import PDFmetadata
from backend.Count import Count
from backend.ClassInformation import ClassInformation


"""

"""
class Document:

    io = FilesIO()

    _dataFolder = 'data/'
    _detailsFile = _dataFolder + 'documentDetails0.csv'
    _pretextFolder = _dataFolder + 'text/before/'
    _textFolder = _dataFolder + 'text/after/'
    _wordsFolder = _dataFolder + 'word/list/'
    _countFolder = _dataFolder + 'word/count/'
    _frequenciesFolder = _dataFolder + 'word/frequency/'

    def __init__(self, filename, title, journal, date, test, hrRat, ipRat,   \
            userRat, creatorRat):
        """

        """
        self._filename = filename
        self._pdfText = PDFtext(filename)
        self._pdfMetadata =                                                  \
            PDFmetadata(filename, self._pdfText, title, journal, date)
        self._count = Count(filename, self._pdfText.getText())
        self._classInformation = ClassInformation(test, hrRat, ipRat,        \
            userRat, creatorRat, self._pdfMetadata.getJournal())
        self.io.outputDocumentData(filename, self)


    def getFilename(self):
        """

        """
        return self._filename


    def getPDFtext(self):
        """

        """
        return self._pdfText


    def getPDFmetadata(self):
        """

        """
        return self._pdfMetadata


    def getCount(self):
        """

        """
        return self._count


    def getClassInformation(self):
        """

        """
        return self._classInformation
