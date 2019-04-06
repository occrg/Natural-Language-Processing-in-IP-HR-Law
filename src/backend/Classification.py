import random
from sklearn import svm
import numpy as np
from sklearn.model_selection import cross_val_score

from backend.FilesIO import FilesIO
from backend.Tokeniser import Tokeniser


"""

"""
class Classification:

    io = FilesIO()

    _dataFolder = 'data/'
    _keyWordsFolder = _dataFolder + 'lists/'
    _userPhrasesPath = _keyWordsFolder + 'User-keyPhrases.txt'
    _creatorPhrasesPath = _keyWordsFolder + 'Creator-keyPhrases.txt'


    def __init__(self, documentList):
        """

        """
        documents = documentList.getDocuments()
        print("assigning test documents")
        trainDocuments, testDocuments =                                      \
            self.assignTestsRandomly(0.25, documents)
        print("formulating Xtrain")
        Xtrain, Ytrain = self.__formulateXY(trainDocuments, documentList)
        print("training data")
        self._clf = self.__trainData(Xtrain, Ytrain)
        print("formulating Xtest")
        Xtest, Ytest = self.__formulateXY(testDocuments, documentList)
        print("testing data")
        self._testScore = self.__testData(Xtest, Ytest, testDocuments)
        print("assigning user-creator ratings")
        self.__userCreatorRatings(testDocuments)
        self._crossValScore =                                                \
            self.__crossValidation(Xtrain, Xtest, Ytrain, Ytest)
        print(self._crossValScore)
        print("saving")
        for document in documents:
            self.io.outputDocumentData(document.getFilename(), document)



    def assignTestsRandomly(self, prop, documents):
        """

        """
        for document in documents:
            document.getClassInformation().setTest(0)
            document.getClassInformation().setHrRat(-1)
            document.getClassInformation().setIpRat(-1)
            document.getClassInformation().setCreatorRat(-1)
            document.getClassInformation().setUserRat(-1)

        trainDocuments = documents.copy()
        testDocuments = []
        testNum = int(prop * len(documents))
        for i in range(testNum):
            document = random.choice(trainDocuments)
            testDocuments.append(document)
            trainDocuments.remove(document)
            document.getClassInformation().setTest(1)
        return trainDocuments, testDocuments


    def __formulateXY(self, documents, documentList):
        """

        """
        allWords = documentList.deduceAllWords()
        X = np.zeros((len(documents), len(allWords)))
        Y = []
        for (r, document) in enumerate(documents):
            for (w, f) in document.getCount().getWordsCountZip():
                X[r][allWords.index(w)] = f
            Y.append(document.getClassInformation().getGt())
        print(X)
        return X, Y


    def __trainData(self, X, Y):
        """

        """
        clf = svm.SVC(gamma='scale', probability=True)
        clf.fit(X, Y)
        return clf

    def __testData(self, X, Y, testDocuments):
        """

        """
        probabilities = self._clf.predict_proba(X)
        for (r, document) in enumerate(testDocuments):
            document.getClassInformation().setHrRat(probabilities[r][0])
            document.getClassInformation().setIpRat(probabilities[r][1])
        return self._clf.score(X, Y)


    def __crossValidation(self, Xtrain, Xtest, Ytrain, Ytest):
        print("formulating Xall and Yall")
        X = np.append(Xtrain, Xtest, axis=0)
        Y = Ytrain.copy()
        Y.extend(Ytest)
        crossValScore =                                                      \
            cross_val_score(estimator=self._clf, X=X, y=Y, cv=5)
        return crossValScore


    def __userCreatorRatings(self, documents):
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
