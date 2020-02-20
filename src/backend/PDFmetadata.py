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


        Returns:
        filename (string)
            --
        pdfText  (PDFtext)
            --
        title    (string)
            --
        journal  (string)
            --
        date     (string)
            --
        """
        self._journal, period = self.__initialiseJournal(filename, journal, pdfText)
        self._title = self.__initialiseTitle(filename, title, journal, period, pdfText.getPretext())
        self._date = self.__initialiseDate(filename, date, journal, period, pdfText.getPretext())


    def getJournal(self):
        """
        Returns:
        self._journal (string)
            --
        """
        return self._journal

    def setJournal(self, journal):
        """
        Arguments:
        journal (string)
            --
        """
        self._journal = journal


    def getTitle(self):
        """
        Returns:
        self._title (string)
            --
        """
        return self._title

    def setTitle(self, title):
        """
        Arguments:
        title (string)
            --
        """
        self._title = title

    def getDate(self):
        """


        Returns:
        self._date (datetime.date)
            --
        """
        if isinstance(self._date, str):
            self._date = datetime.datetime(int(self._date[0:4]), int(self._date[5:7]), int(self._date[8:10])).date()
        return self._date

    def setDate(self, date):
        """
        Arguments:
        date (datetime.date || string)
            --
        """
        self._date = date

    def __initialiseJournal(self, filename, journal, pdfText):
        """


        Arguments:
        filename (string)
            --
        journal  (string)
            --
        pdfText  (PDFtext)
            --

        Returns:
        journal (string)
            --
        period  (string)
            --
        """
        journal, period = self.converter.extractJournalFromText(journal, pdfText.getPretext(), filename)
        if pdfText.getText() == "-":
            pdfText.cleanText(filename, journal)
        return journal, period


    def __initialiseTitle(self, filename, title, journal, period, text):
        """


        Arguments:
        filename (string)
            --
        title    (string)
            --
        journal  (string)
            --
        period   (string)
            --

        Returns:
        title (string)
            --
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


        Arguments:
        filename (string)
            --
        date     (string)
            --
        journal  (string)
            --
        period   (string)
            --
        text     (string)
            -- 
        """
        if date == "-":
            date = self.converter.extractDateFromText(journal, period, text)
            date = self.converter.getDateFromPDFmetadata(filename, date, journal)
        else:
            date = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10])).date()
        return date
