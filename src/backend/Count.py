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
    _wordFolder = _dataFolder + 'word/list/'
    _countFolder = _dataFolder + 'word/count/'
    _frequencyFolder = _dataFolder + 'word/frequency/'

    def __init__(self, filename, text):
        """

        """
        self._words = self.__initialiseWords(filename, text)
        self._count = self.__initialiseCount(filename, text)
        self.io.listToLineSeparated(self._words, self._wordFolder + filename + '.txt')
        self.io.listToLineSeparated(self._count, self._countFolder + filename + '.txt')


    def calculateFrequency(self, filename, wordLists):
        """

        """
        self._frequency = self.io.lineSeparatedToList(self._frequencyFolder + filename + '.txt')
        if self._frequency == []:
            wordCount = getWordsCountZip()
            self._frequency = self.frequencyCalc.tfidf(wordCount, wordLists)
        self.io.listToLineSeparated(self._frequency, self._frequencyFolder + filename + '.txt')


    def getWords(self):
        """

        """
        return self._words

    def getCount(self):
        """

        """
        return self._count

    def getWordsCountZip(self):
        """

        """
        return list(zip(self._words, self._count))


    def getWordsFrequencyZip(self):
        """

        """
        return list(zip(self._words, self._frequency))


    def setFrequency(self, frequency):
        self._frequency = frequency


    def __initialiseWords(self, filename, text):
        """

        """
        uniqueWords = self.io.lineSeparatedToList(self._wordFolder + filename + '.txt')
        if uniqueWords == []:
            for w in self.tokeniser.splitByWord(text):
                if w not in uniqueWords:
                    uniqueWords.append(w)
        return uniqueWords


    def __initialiseCount(self, filename, text):
        """

        """
        wordCounts = self.io.lineSeparatedToList(self._countFolder + filename + '.txt')
        if wordCounts == []:
            for w in self._words:
                wordCounts.append(self.tokeniser.splitByWord(text).count(w))
        return wordCounts
