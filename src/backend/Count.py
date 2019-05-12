from backend.FilesIO import FilesIO
from backend.Tokeniser import Tokeniser
from backend.FrequencyCalc import FrequencyCalc

"""

"""
class Count:

    io = FilesIO()
    tokeniser = Tokeniser()
    frequencyCalc = FrequencyCalc()

    _dataFolder = 'data/'
    _wordsFolder = _dataFolder + 'word/'
    _featureFolder = _wordsFolder + 'feature/'
    _countFolder = _wordsFolder + 'count/'
    _tfFolder = _wordsFolder + 'tf/'
    _idfFolder = _wordsFolder + 'idf/'
    _tfidfFolder = _wordsFolder + 'tfidf/'
    _tfidfcfFolder = _wordsFolder + 'tfidfcf/'


    def __init__(self, filename, text):
        """

        """
        text = self.tokeniser.splitByWord(text)
        self._textList = self.tokeniser.removeStopwords(text)
        self.__initialiseFeatures(filename)
        self.__initialiseCount(filename)
        self.__iniialiseTf(filename)


    def calculateTfidfCf(self, filename, classWordLists, nonClassWordLists):
        """

        """
        allWordLists = classWordLists.copy()
        allWordLists.extend(nonClassWordLists)
        idfStrings = self.io.lineSeparatedToList(self._idfFolder + filename + '.txt')
        if idfStrings == []:
            self._idf = self.frequencyCalc.idf(self._features, allWordLists)
            self.io.listToLineSeparated(self._idf, self._idfFolder + filename + '.txt')
        else:
            self._idf = list(map(float, idfStrings))
        tfidfStrings = self.io.lineSeparatedToList(self._tfidfFolder + filename + '.txt')
        if tfidfStrings == []:
            self._tfidf = self.frequencyCalc.tfidf(self._tf, self._idf)
            self.io.listToLineSeparated(self._tfidf, self._tfidfFolder + filename + '.txt')
        else:
            self._tfidf = list(map(float, tfidfStrings))
        tfidfcfStrings = self.io.lineSeparatedToList(self._tfidfcfFolder + filename + '.txt')
        if tfidfcfStrings == []:
            self._tfidfcf = self.frequencyCalc.tfidfcf(self.getFeaturesTfidfZip(), classWordLists)
            self.io.listToLineSeparated(self._tfidfcf, self._tfidfcfFolder + filename + '.txt')
        else:
            self._tfidfcf = list(map(float, tfidfcfStrings))


    def getFeatures(self):
        """

        """
        return self._features

    def getCount(self):
        """

        """
        return self._count

    def getFeaturesCountZip(self):
        """

        """
        return list(zip(self._features, self._count))

    def getFeaturesTfZip(self):
        """

        """
        return list(zip(self._features, self._tf))

    def getFeaturesIdfZip(self):
        """

        """
        return list(zip(self._features, self._idf))

    def getFeaturesTfidfZip(self):
        """

        """
        return list(zip(self._features, self._tfidf))

    def getFeaturesTfidfcfZip(self):
        """

        """
        return list(zip(self._features, self._tfidfcf))

    def setFrequency(self, frequency):
        self._frequency = frequency


    def __initialiseFeatures(self, filename):
        """

        """
        self._features = self.io.lineSeparatedToList(self._featureFolder + filename + '.txt')
        if self._features == []:
            for w in self._textList:
                if w not in self._features:
                    self._features.append(w)
            self.io.listToLineSeparated(self._features, self._featureFolder + filename + '.txt')


    def __initialiseCount(self, filename):
        """

        """
        self._count = []
        countStrings = self.io.lineSeparatedToList(self._countFolder + filename + '.txt')
        if countStrings == []:
            for w in self._features:
                self._count.append(self._textList.count(w))
            self.io.listToLineSeparated(self._count, self._countFolder + filename + '.txt')
        else:
            self._count = list(map(int, countStrings))


    def __iniialiseTf(self, filename):
        """

        """
        tfStrings = self.io.lineSeparatedToList(self._tfFolder + filename + '.txt')
        if tfStrings == []:
            self._tf = self.frequencyCalc.tf(self.getFeaturesCountZip())
            self.io.listToLineSeparated(self._tf, self._tfFolder + filename + '.txt')
        else:
            self._tf = list(map(float, tfStrings))
