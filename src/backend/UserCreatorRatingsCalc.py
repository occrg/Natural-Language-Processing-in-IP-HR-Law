from backend.FilesIO import FilesIO
from backend.Tokeniser import Tokeniser


"""

"""
class UserCreatorRatingsCalc:

    io = FilesIO()
    tokeniser = Tokeniser()

    _dataFolder = 'data/'
    _keyWordsFolder = _dataFolder + 'lists/'
    _userPhrasesPath = _keyWordsFolder + 'User-keyPhrases.txt'
    _creatorPhrasesPath = _keyWordsFolder + 'Creator-keyPhrases.txt'
    _comparativePosPath = _keyWordsFolder + 'comparatives-pos.txt'
    _comparativeNegPath = _keyWordsFolder + 'comparatives-neg.txt'
    _superlativePosPath = _keyWordsFolder + 'superlatives-pos.txt'
    _superlativeNegPath = _keyWordsFolder + 'superlatives-neg.txt'
    _negatorsPath = _keyWordsFolder + 'negators.txt'


    def userCreatorProportion(self, documents):
        """

        """
        creatorPhrases =                                                     \
            self.io.lineSeparatedToList(self._creatorPhrasesPath)
        userPhrases =                                                        \
            self.io.lineSeparatedToList(self._userPhrasesPath)
        comparativePosPhrases =                                              \
            self.io.lineSeparatedToList(self._comparativePosPath)
        comparativeNegPhrases =                                              \
            self.io.lineSeparatedToList(self._comparativeNegPath)
        superlativePosPhrases =                                              \
            self.io.lineSeparatedToList(self._superlativePosPath)
        superlativeNegPhrases =                                              \
            self.io.lineSeparatedToList(self._superlativeNegPath)
        negatorsPhrases =                                                    \
            self.io.lineSeparatedToList(self._negatorsPath)
        tokeniser = Tokeniser()
        for document in documents:
            userRatTot = 0
            creatorRatTot = 0
            text = document.getPDFtext().getText()
            sentences = tokeniser.splitBySentence(text)
            for sentence in sentences:
                scale = 1
                userBin = 0
                creatorBin = 0
                words = tokeniser.splitByWord(sentence)
                for word in words:
                    if word in userPhrases:
                        userBin = 1
                    if word in creatorPhrases:
                        creatorBin = 1
                userRatSent = userBin * scale
                creatorRatSent = creatorBin * scale
                userRatTot += userRatSent
                creatorRatTot += creatorRatSent
            userRatMean = userRatTot / len(sentences)
            creatorRatMean = creatorRatTot / len(sentences)
            document.getClassInformation().setUserRat(userRatMean)
            document.getClassInformation().setCreatorRat(creatorRatMean)
            self.io.outputDocumentData(document)


    def userCreatorScore(self, documents):
        """

        """
        creatorPhrases =                                                     \
            self.io.lineSeparatedToList(self._creatorPhrasesPath)
        userPhrases =                                                        \
            self.io.lineSeparatedToList(self._userPhrasesPath)
        comparativePosPhrases =                                              \
            self.io.lineSeparatedToList(self._comparativePosPath)
        comparativeNegPhrases =                                              \
            self.io.lineSeparatedToList(self._comparativeNegPath)
        superlativePosPhrases =                                              \
            self.io.lineSeparatedToList(self._superlativePosPath)
        superlativeNegPhrases =                                              \
            self.io.lineSeparatedToList(self._superlativeNegPath)
        negatorsPhrases =                                                    \
            self.io.lineSeparatedToList(self._negatorsPath)
        tokeniser = Tokeniser()
        for document in documents:
            userRatTot = 0
            creatorRatTot = 0
            text = document.getPDFtext().getText()
            sentences = tokeniser.splitBySentence(text)
            for sentence in sentences:
                scale = 1
                userBin = 0
                creatorBin = 0
                words = tokeniser.splitByWord(sentence)
                for word in words:
                    if word in userPhrases:
                        userBin = 1
                    if word in creatorPhrases:
                        creatorBin = 1
                    if word in comparativePosPhrases:
                        scale += 0.35
                    if word in comparativeNegPhrases:
                        scale -= 0.35
                    if word in superlativePosPhrases:
                        scale += 0.65
                    if word in superlativeNegPhrases:
                        scale -= 0.65
                    if word in negatorsPhrases:
                        scale *= -1
                userRatSent = userBin * scale
                creatorRatSent = creatorBin * scale
                if (not userRatSent == 0) or (not creatorRatSent == 0):
                    print('(%f,%f): %s' % (userRatSent, creatorRatSent, sentence))
                userRatTot += userRatSent
                creatorRatTot += creatorRatSent
            userRatMean = userRatTot / len(sentences)
            creatorRatMean = creatorRatTot / len(sentences)
            document.getClassInformation().setUserRat(userRatMean)
            document.getClassInformation().setCreatorRat(creatorRatMean)
            self.io.outputDocumentData(document)
