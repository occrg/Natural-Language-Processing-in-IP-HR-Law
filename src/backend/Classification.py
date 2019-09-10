from backend.FilesIO import FilesIO
from backend.Tokeniser import Tokeniser
from backend.ClassificationTools import ClassificationTools


"""
Performs HR-IP classifications on a DocumentList object and stores its
evaluation data.
"""
class Classification:

    io = FilesIO()
    classTools = ClassificationTools()


    def __init__(self):
        """
        Initialise a Classification object from stored file.
        """
        self._testScore, self._tp, self._tn, self._fp, self._fn =            \
            self.io.retrieveVisualisationEvaluationData()


    def classifyDocuments(self, documentList):
        """
        Train and test documents in $documentList.

        Arguments:
        documentList (DocumentList)
            -- the DocumentList object containing the information of
               the documents to be classified
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
        self._testScore = self.classTools.balancedAccuracy(                  \
            self._tp, self._tn, self._fp, self._fn)
        print("output")
        for document in documentList.getDocuments():
            self.io.outputDocumentData(document)
        self.io.outputVisualisationEvaluationData(self)


    def getTestScore(self):
        """
        Returns:
        self._testScore (float)
            -- Score of classification
        """
        return self._testScore

    def getTFPNs(self):
        """
        Returns:
        self._tp (int)
            -- the number of true positives of the classification
        self._tn (int)
            -- the number of true negatives of the classification
        self._fp (int)
            -- the number of false positives of the classification
        self._fn (int)
            -- the number of false negatives of the classification
        """
        return self._tp, self._tn, self._fp, self._fn


    def __splitDocuments(self, documentList):
        """
        Reconstructs the data in $documentList into data compatible
        with scikit learn classification functions.

        Arguments:
        documentList  (DocumentList)

        Returns:
        testDocuments ([Document])
            -- the list of Document objects the classification is to be
               tested against
        Xtrain        (np.array)
            -- the matrix of feature counts for the training data
        Ytain         ([int])
            -- the classes of the training data
        Xtest         (np.array)
            -- the matrix of feature counts for the test data
        Ytest         (np.array)
            -- the classes of the test data
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
        Assigns the probabilities calculated during classification to
        each Document object in $testDocuments

        Arguments:
        probabilities ([(float,float)])
            -- a list of tuples where each probability represents a
               different class
        testDocuments ([Document])
            -- the list of Document objects that the classification was
               tested against
        """
        for (r, document) in enumerate(testDocuments):
            document.getClassInformation().setHrRat(probabilities[r][0])
            document.getClassInformation().setIpRat(probabilities[r][1])
