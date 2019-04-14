import re

from backend.FilesIO import FilesIO
from backend.PDFconverter import PDFconverter


"""

"""
class PDFtext:

    io = FilesIO()
    converter = PDFconverter()

    _dataFolder = 'data/'
    _pdfFolder = _dataFolder + 'pdf/'
    _pretextFolder = _dataFolder + 'text/before/'
    _textFolder = _dataFolder + 'text/after/'

    def __init__(self, filename):
        """

        """
        self._pretext = self.__initialisePretext(filename)
        self._text = self.__initialiseText(filename)

    def getPretext(self):
        """

        """
        return self._pretext

    def cleanText(self, filename, journal):
        """

        """
        text = self.converter.removeMetadataFromText(self._pretext, journal)
        text = self.converter.substituteKerning(text)
        self._text = text
        self.io.stringToTXTfile(self._text, self._textFolder + filename + '.txt')


    def getText(self):
        return self._text


    def __initialisePretext(self, filename):
        """

        """
        pretext = self.io.txtFileToString(self._pretextFolder + filename + '.txt')
        if pretext == "-":
            pretext = self.converter.pdfToString(filename)
        self.io.stringToTXTfile(pretext, self._pretextFolder + filename + '.txt')
        return pretext


    def __initialiseText(self, filename):
        """

        """
        text = self.io.txtFileToString(self._textFolder + filename + '.txt')
        return text
