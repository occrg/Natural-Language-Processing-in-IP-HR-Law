import random
import math
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


    def __init__(self):
        """

        """
        self._testScore, self._crossValScore = self.io.retrieveEvaluationData()


    def classifyDocuments(self, documentList):
        """

        """
        documents = documentList.getDocuments()
        trainDocuments = documentList.getTrainTestDocuments(0)
        testDocuments = documentList.getTrainTestDocuments(1)
        print("formulating XYTrain")
        Xtrain, Ytrain = self.__formulateXY(trainDocuments, documentList)
        print("training")
        self._clf = self.__trainData(Xtrain, Ytrain)
        print("formulating XYTest")
        Xtest, Ytest = self.__formulateXY(testDocuments, documentList)
        print("precit probabilities")
        probsTest = self._clf.predict_proba(Xtest)
        self.__assignProbabilities(probsTest, testDocuments)
        print("calculating score")
        self._tp, self._tn, self._fp, self._fn = self.__evaluateClassification(probsTest, Ytest)
        self._testScore = self.__percentageCorrect(self._tp, self._tn, self._fp, self._fn)
        print("user creator")
        self.__userCreatorRatings(testDocuments)
        print("formulating XYall")
        Xall = np.append(Xtrain, Xtest, axis=0)
        Yall = Ytrain.copy()
        Yall.extend(Ytest)
        print("cross validating")
        self._crossValScore =                                                \
            self.__crossValidation(Xall, Yall, 4)
        print("output")
        for document in documents:
            self.io.outputDocumentData(document)
        self.io.outputEvaluationData(self)


    def getTestScore(self):
        """

        """
        return self._testScore

    def getCrossValScore(self):
        """

        """
        return self._crossValScore


    def __formulateXY(self, documents, documentList):
        """

        """
        allFeatures = documentList.getAllFeatures()
        X = np.zeros((len(documents), len(allFeatures)))
        Y = []
        for (r, document) in enumerate(documents):
            for (w, f) in document.getCount().getFeaturesTfidfZip():
                X[r][allFeatures.index(w)] = f
            Y.append(document.getClassInformation().getGt())
        return X, Y


    def __trainData(self, X, Y):
        """

        """
        clf = svm.SVC(gamma='scale', probability=True)
        clf.fit(X, Y)
        return clf

    def __assignProbabilities(self, probabilities, testDocuments):
        """

        """
        for (r, document) in enumerate(testDocuments):
            document.getClassInformation().setHrRat(probabilities[r][0])
            document.getClassInformation().setIpRat(probabilities[r][1])

    def __evaluateClassification(self, probsTest, Ytest):
        """

        """
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for i in range(len(probsTest)):
            if Ytest[i] == 1 and probsTest[i][1] > probsTest[i][0]:
                tp += 1
            if Ytest[i] == 1 and not probsTest[i][1] > probsTest[i][0]:
                fn += 1
            if Ytest[i] == 0 and probsTest[i][1] < probsTest[i][0]:
                tn += 1
            if Ytest[i] == 0 and not probsTest[i][1] < probsTest[i][0]:
                fp += 1
        return tp, tn, fp, fn

    def __percentageCorrect(self, tp, tn, fp, fn):
        """

        """
        return (tp + tn) / (tp + tn + fp + fn)


    def __crossValidation(self, Xall, Yall, split):
        """

        """
        crossValScore = []
        allIndexes = list(range(len(Xall)))
        remainingIndexes = allIndexes.copy()
        testNum = math.floor(len(Xall) / split)
        for i in range(split):
            print("\ncalculating score %d" % i)
            if i == split-1:
                testIndexes = remainingIndexes
                testNum = len(testIndexes)
                trainIndexes = [x for x in allIndexes if x not in testIndexes]
            else:
                testIndexes = []
                trainIndexes = allIndexes.copy()
                for n in range(testNum):
                    ele = random.choice(remainingIndexes)
                    testIndexes.append(ele)
                    trainIndexes.remove(ele)
                    remainingIndexes.remove(ele)
            Xtest = np.empty((len(testIndexes), Xall.shape[1]))
            Xtrain = np.empty((len(trainIndexes), Xall.shape[1]))
            Ytest = []
            Ytrain = []
            for i, n in enumerate(testIndexes):
                Xtest[i,:] = Xall[n,:]
                Ytest.append(Yall[n])
            for i, n in enumerate(trainIndexes):
                Xtrain[i:,] = Xall[n,:]
                Ytrain.append(Yall[n])

            print("training data")
            clf = self.__trainData(Xtrain, Ytrain)
            print("predicting probabilities")
            probsTest = clf.predict_proba(Xtest)
            print("calculating score")
            tp, tn, fp, fn = self.__evaluateClassification(probsTest, Ytest)
            crossValScore.append(self.__percentageCorrect(tp, tn, fp, fn))
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
