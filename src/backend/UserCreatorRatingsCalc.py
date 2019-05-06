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


    def userCreatorRatings(self, documents):
        """

        """
        creatorPhrases = self.io.lineSeparatedToList(self._creatorPhrasesPath)
        userPhrases = self.io.lineSeparatedToList(self._userPhrasesPath)
        tokeniser = Tokeniser()
        for document in documents:
            text = document.getPDFtext().getText()
            sentences = tokeniser.splitBySentence(text)
            creatorSentences = tokeniser.removeSentencesWithoutPhrases(      \
                creatorPhrases, sentences)
            userSentences = tokeniser.removeSentencesWithoutPhrases(         \
                userPhrases, sentences)
            creatorProp = len(creatorSentences) / len(sentences)
            userProp = len(userSentences) / len(sentences)
            document.getClassInformation().setCreatorRat(creatorProp)
            document.getClassInformation().setUserRat(userProp)
            self.io.outputDocumentData(document)
