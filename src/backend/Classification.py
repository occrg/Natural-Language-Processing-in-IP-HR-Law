from backend.FilesIO import FilesIO
from backend.Tokeniser import Tokeniser
from backend.ClassificationTools import ClassificationTools


"""

"""
class Classification:

    io = FilesIO()
    classTools = ClassificationTools()


    def __init__(self):
        """

        """
        self._testScore, self._tp, self._tn, self._fp, self._fn =            \
            self.io.retrieveVisualisationEvaluationData()


    def classifyDocuments(self, documentList):
        """

        """
        testDocuments, Xtrain, Ytrain, Xtest, Ytest =                        \
            self.__splitDocuments(documentList)
        print("training")
        self._clf = self.classTools.trainData(Xtrain, Ytrain)
        print("precit probabilities")
        probsTest = self._clf.predict_proba(Xtest)
        self.__assignProbabilities(probsTest, testDocuments)
        print("calculating score")
        self._tp, self._tn, self._fp, self._fn =                             \
            self.classTools.evaluateClassification(probsTest, Ytest)
        self._testScore = self.classTools.balancedAccuracy(                       \
            self._tp, self._tn, self._fp, self._fn)
        print("output")
        for document in documentList.getDocuments():
            self.io.outputDocumentData(document)
        self.io.outputVisualisationEvaluationData(self)


    def getTestScore(self):
        """

        """
        return self._testScore

    def getTFPNs(self):
        """

        """
        return self._tp, self._tn, self._fp, self._fn


    def __splitDocuments(self, documentList):
        """

        """
        documents = documentList.getDocuments()
        trainDocuments = documentList.getTrainTestDocuments(0)
        testDocuments = documentList.getTrainTestDocuments(1)
        print("formulating XYTrain")
        Xtrain, Ytrain = self.classTools.formulateXY(trainDocuments, documentList)
        print("formulating XYTest")
        Xtest, Ytest = self.classTools.formulateXY(testDocuments, documentList)
        return testDocuments, Xtrain, Ytrain, Xtest, Ytest


    def __assignProbabilities(self, probabilities, testDocuments):
        """

        """
        for (r, document) in enumerate(testDocuments):
            document.getClassInformation().setHrRat(probabilities[r][0])
            document.getClassInformation().setIpRat(probabilities[r][1])
