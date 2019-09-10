from backend.FilesIO import FilesIO
from backend.Tokeniser import Tokeniser
from backend.FrequencyCalc import FrequencyCalc

"""
Stores data relating to feature counts of parent Document object.
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
        Initialises a Count object. Gets data from file if file exists,
        otherwise, process it from $text.

        Arguments:
        filename  (str)
            -- the filename of the parent Document object
        text      (str)
            -- the text in the article of the parent Document object
        """
        text = self.tokeniser.splitByWord(text)
        self._textList = self.tokeniser.removeStopwords(text)
        self.__initialiseFeatures(filename)
        self.__initialiseCount(filename)
        self.__iniialiseTf(filename)


    def calculateTfidfCf(self, filename, classWordLists, nonClassWordLists):
        """
        If file exists, get tf-idf-cf from file. If not, calculate it based
        on self._tf and self._tfidf.

        Arguments:
        filename           (str)
            -- the filename of the parent Document object
        classWordLists     ([[str]])
            -- a list of list of strings with each list representing
               the features of a document in the class of the parent
               Document object and each string representing a feature
               in that Document object
        nonClassWordLists  ([[str]])
            -- a list of list of strings with each list representing
               the features of a document not in the class of the
               parent Document object and each string representing a
               feature in that Document object
        """
        allWordLists = classWordLists.copy()
        allWordLists.extend(nonClassWordLists)
        idfStrings =                                                         \
            self.io.lineSeparatedToList(self._idfFolder + filename + '.txt')
        if idfStrings == []:
            self._idf = self.frequencyCalc.idf(self._features, allWordLists)
            self.io.listToLineSeparated(
                self._idf, self._idfFolder + filename + '.txt')
        else:
            self._idf = list(map(float, idfStrings))
        tfidfStrings = self.io.lineSeparatedToList(
            self._tfidfFolder + filename + '.txt')
        if tfidfStrings == []:
            self._tfidf = self.frequencyCalc.tfidf(self._tf, self._idf)
            self.io.listToLineSeparated(                                     \
                self._tfidf, self._tfidfFolder + filename + '.txt')
        else:
            self._tfidf = list(map(float, tfidfStrings))
        tfidfcfStrings = self.io.lineSeparatedToList(                        \
            self._tfidfcfFolder + filename + '.txt')
        if tfidfcfStrings == []:
            self._tfidfcf = self.frequencyCalc.tfidfcf(                      \
                self.getFeaturesTfidfZip(), classWordLists)
            self.io.listToLineSeparated(                                     \
                self._tfidfcf, self._tfidfcfFolder + filename + '.txt')
        else:
            self._tfidfcf = list(map(float, tfidfcfStrings))


    def getFeatures(self):
        """
        Returns:
        self._features  ([str])
            -- a list of strings with each string representing a unique
               feature of the parent Document object
        """
        return self._features

    def getCount(self):
        """
        Returns:
        self._count  ([int])
            -- a list of integers with the ith integer representing the
               number of occurrences of the ith string in
               self._features in the parent Document object
        """
        return self._count

    def getFeaturesCountZip(self):
        """
        Returns:
        zipped:  ([(str, int)])
            -- a list of tuples where the first member of the tuple is
               a feature of the parent Document object and the second
               member is the number of occurrences that the feature
               has in the parent Document object
        """
        zipped = list(zip(self._features, self._count))
        return zipped

    def getFeaturesTfZip(self):
        """
        Returns:
        zipped:  ([(str, float)])
            -- a list of tuples where the first member of the tuple is
               a feature of the parent Document object and the second
               member is the term frequency that the feature has in the
               parent Document object
        """
        zipped = list(zip(self._features, self._tf))
        return zipped

    def getFeaturesIdfZip(self):
        """
        Returns:
        zipped:  ([(str, float)])
            -- a list of tuples where the first member of the tuple is
               a feature of the parent Document object and the second
               member is the inverse document frequency that the
               feature has in the parent Document object
        """
        zipped = list(zip(self._features, self._idf))
        return zipped

    def getFeaturesTfidfZip(self):
        """
        Returns:
        zipped:  ([(str, float)])
            -- a list of tuples where the first member of the tuple is
               a feature of the parent Document object and the second
               member is the term frequency-inverse document frequency
               that the feature has in the parent Document object
        """
        zipped = list(zip(self._features, self._tfidf))
        return zipped

    def getFeaturesTfidfcfZip(self):
        """
        Returns:
        zipped:  ([(str, float)])
            -- a list of tuples where the first member of the tuple is
               a feature of the parent Document object and the second
               member is the term frequency-inverse document frequency-
               class frequency that the feature has in the parent
               Document object
        """
        zipped = list(zip(self._features, self._tfidfcf))
        return zipped


    def __initialiseFeatures(self, filename):
        """
        Initialises self._features. Retrieves from file if file exists.
        Otherwise, calculates from self._textList.

        Arguments:
        filename  (str)
            -- the filename of the parent Document object
        """
        self._features = self.io.lineSeparatedToList(                        \
            self._featureFolder + filename + '.txt')
        if self._features == []:
            for w in self._textList:
                if w not in self._features:
                    self._features.append(w)
            self.io.listToLineSeparated(                                     \
                self._features, self._featureFolder + filename + '.txt')


    def __initialiseCount(self, filename):
        """
        Initialises self._count. Retrieves from file if file exists.
        Otherwise, calculates from self._textList.

        Arguments:
        filename  (str)
            -- the filename of the parent Document object
        """
        self._count = []
        countStrings = self.io.lineSeparatedToList(                          \
            self._countFolder + filename + '.txt')
        if countStrings == []:
            for w in self._features:
                self._count.append(self._textList.count(w))
            self.io.listToLineSeparated(                                     \
                self._count, self._countFolder + filename + '.txt')
        else:
            self._count = list(map(int, countStrings))


    def __iniialiseTf(self, filename):
        """
        Initialises self._tf. Retrieves from file if file exists.
        Otherwise, calculates from self._textList.

        Arguments:
        filename  (str)
            -- the filename of the parent Document object
        """
        tfStrings = self.io.lineSeparatedToList(                             \
            self._tfFolder + filename + '.txt')
        if tfStrings == []:
            self._tf = self.frequencyCalc.tf(                                \
                self.getFeaturesCountZip())
            self.io.listToLineSeparated(                                     \
                self._tf, self._tfFolder + filename + '.txt')
        else:
            self._tf = list(map(float, tfStrings))
