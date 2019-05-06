import numpy as np
import random as rnd
import math
import copy

from backend.ClassificationTools import ClassificationTools
from backend.TrendTools import TrendTools
from backend.FilesIO import FilesIO


"""

"""
class CrossValidation:

    io = FilesIO()
    classTools = ClassificationTools()
    trendTools = TrendTools()


    def __init__(self):
        """

        """
        self._crossValScore, self._trendsCrossVal =                          \
            self.io.retrieveCrossValEvaluationData()


    def crossValidateAll(self, documentList, split):
        """

        """
        documents = documentList.getDocuments()
        trainIndexesList, testIndexesList =                                  \
            self.__calculateIndexes(split, len(documents))
        Xall, Yall = self.classTools.formulateXY(documents, documentList)
        testDocumentsLists = self.__trainSegments(                           \
            Xall, Yall, trainIndexesList, testIndexesList, documents)
        self.__crossValidateClassifications(testDocumentsLists)
        self.__crossValidatePvalues(testDocumentsLists)
        self.io.outputCrossValEvaluationData(self)

    def getCrossValScore(self):
        """

        """
        return self._crossValScore

    def getTrendsCrossVal(self):
        """

        """
        return self._trendsCrossVal


    def __calculateIndexes(self, split, docsLen):
        """

        """
        trainIndexesList = []
        testIndexesList = []
        allIndexes = list(range(docsLen))
        testNum = math.floor(docsLen / split)
        remainingIndexes = allIndexes.copy()
        for i in range(split):
            if i == split-1:
                testIndexes = remainingIndexes
                testNum = len(testIndexes)
                trainIndexes =                                               \
                    [x for x in allIndexes if x not in testIndexes]
            else:
                testIndexes = []
                trainIndexes = allIndexes.copy()
                for n in range(testNum):
                    ele = rnd.choice(remainingIndexes)
                    testIndexes.append(ele)
                    trainIndexes.remove(ele)
                    remainingIndexes.remove(ele)
            trainIndexesList.append(trainIndexes)
            testIndexesList.append(testIndexes)
        return trainIndexesList, testIndexesList


    def __trainSegments(self, Xall, Yall, trainIndexesList, testIndexesList, \
        documents):
        """

        """
        testDocumentsLists = []
        for i in range(len(trainIndexesList)):
            testDocuments = []
            print("\ntraining document set %d out of %d"                     \
                % (i, len(trainIndexesList)))
            trainIndexes = trainIndexesList[i]
            testIndexes = testIndexesList[i]
            Xtest = np.empty((len(testIndexes), Xall.shape[1]))
            Xtrain = np.empty((len(trainIndexes), Xall.shape[1]))
            Ytest = []
            Ytrain = []
            for j, n in enumerate(testIndexes):
                document = copy.deepcopy(documents[n])
                testDocuments.append(document)
                Xtest[j,:] = Xall[n,:]
                Ytest.append(Yall[n])
            for j, n in enumerate(trainIndexes):
                Xtrain[j,:] = Xall[n,:]
                Ytrain.append(Yall[n])

            print("training data")
            clf = self.classTools.trainData(Xtrain, Ytrain)
            print("predicting probabilities")
            probsTest = clf.predict_proba(Xtest)

            for c, document in enumerate(testDocuments):
                classInfo = document.getClassInformation()
                classInfo.setHrRat(probsTest[c][0])
                classInfo.setIpRat(probsTest[c][1])

            testDocumentsLists.append(testDocuments)
        return testDocumentsLists


    def __crossValidateClassifications(self, testDocumentsLists):
        """

        """
        crossValScore = []
        for testDocuments in testDocumentsLists:
            probsTest = []
            Ytest = []
            for document in testDocuments:
                classInfo = document.getClassInformation()
                probsTest.append((classInfo.getHrRat(), classInfo.getIpRat()))
                Ytest.append(classInfo.getGt())
            tp, tn, fp, fn =                                                 \
                self.classTools.evaluateClassification(probsTest, Ytest)
            crossValScore.append(                                            \
                self.classTools.balancedAccuracy(tp, tn, fp, fn))
        self._crossValScore = crossValScore
        print(self._crossValScore)


    def __crossValidatePvalues(self, testDocumentsLists):
        """

        """
        self._trendsCrossVal = []
        hr_hrip_time_GraphTrends = []
        ip_hrip_time_GraphTrends = []
        hr_usercreator_time_GraphTrends = []
        ip_usercreator_time_GraphTrends = []
        for c, testDocuments in enumerate(testDocumentsLists):
            print("\ncalculating p-values %d out of %d"                      \
                % (c, len(testDocumentsLists)))
            date, hr_ip, user_creator =                                      \
                self.trendTools.arrangeIntoPoints(testDocuments)
            trends =                                                         \
                self.trendTools.generateTrends(date, hr_ip, user_creator)
            hr_hrip_time_GraphTrends.append(trends[0].getPgradient())
            ip_hrip_time_GraphTrends.append(trends[1].getPgradient())
            hr_usercreator_time_GraphTrends.append(trends[2].getPgradient())
            ip_usercreator_time_GraphTrends.append(trends[3].getPgradient())
        self._trendsCrossVal.append(hr_hrip_time_GraphTrends)
        self._trendsCrossVal.append(ip_hrip_time_GraphTrends)
        self._trendsCrossVal.append(hr_usercreator_time_GraphTrends)
        self._trendsCrossVal.append(ip_usercreator_time_GraphTrends)
        print(self._trendsCrossVal)
