import datetime

from backend.FilesIO import FilesIO
from backend.PDFconverter import PDFconverter

"""

"""
class PDFmetadata:

    io = FilesIO()
    converter = PDFconverter()

    _dataFolder = 'data/'
    _pdfFolder = _dataFolder + 'pdf/'


    def __init__(self, filename, pdfText, title, journal, date):
        """

        """
        self._journal, period = self.__initialiseJournal(filename, journal, pdfText)
        self._title = self.__initialiseTitle(filename, title, journal, period, pdfText.getPretext())
        self._date = self.__initialiseDate(filename, date, journal, period, pdfText.getPretext())


    def getJournal(self):
        """

        """
        return self._journal

    def setJournal(self, journal):
        """

        """
        self._journal = journal


    def getTitle(self):
        """

        """
        return self._title

    def setTitle(self, title):
        """

        """
        self._title = title


    def getDate(self):
        """

        """
        return self._date

    def setDate(self, date):
        """

        """
        self._date = date

    def __initialiseJournal(self, filename, journal, pdfText):
        """

        """
        journal, period = self.converter.extractJournalFromText(pdfText.getPretext(), filename)
        if pdfText.getText == "-":
            pdfText.cleanText(filename, journal)
        return journal, period


    def __initialiseTitle(self, filename, title, journal, period, text):
        """

        """
        if title == "-":
            title = self.converter.extractTitleFromText(journal, period, text)
            if title == "-":
                title = self.converter.getTitleFromPDFmetadata(filename)
        title = title.replace(',', '')
        title = title.replace('\n', ' ')
        return title


    def __initialiseDate(self, filename, date, journal, period, text):
        """

        """
        if date == "-":
            date = self.converter.extractDateFromText(journal, period, text)
            date = self.converter.getDateFromPDFmetadata(filename, date, journal)
        else:
            date = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10])).date()
        return date
