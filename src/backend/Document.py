from backend.FilesIO import FilesIO
from backend.PDFtext import PDFtext
from backend.PDFmetadata import PDFmetadata
from backend.Count import Count
from backend.ClassInformation import ClassInformation


"""

"""
class Document:

    io = FilesIO()


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
        self.io.outputDocumentData(self)


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


    def makeFormChanges(self, title, date, journal, test):
        """

        """
        self._pdfMetadata.setTitle(title)
        self._pdfMetadata.setDate(date)
        self._classInformation.setTest(test)
        if not journal == self.getPDFmetadata().getJournal():
            self._pdfMetadata.setJournal(journal)
            self._pdfText.cleanText(self._filename, journal)
        self.io.outputDocumentData(self)

    def removeData(self):
        self.io.removeDocumentData(self._filename)
        self.io.removeAssociatedFiles(self._filename)
