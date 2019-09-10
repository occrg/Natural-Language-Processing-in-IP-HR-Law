from sklearn import svm
import numpy as np


"""
Performs computations related to classification.
"""
class ClassificationTools:


    def formulateXY(self, documents, documentList):
        """
        Restructures $documents data so it can be inputted into
        scikitlearn functions.

        Arguments:
        documents    ([Document])
            -- a list of Document objects that are to be restructured
        documentList (DocumentList)
            -- the DocumentList object that contains the list of
               features the model uses

        Returns:
        X             (np.array)
            -- a matrix where each row represents a different Document
               object from $documents and each column represents a
               different feature from the training documents in
               $documentList
        Y             ([int])
            -- a list of integers that indicate the ordered ground
               truth of each Document object in $documents
        """
        features = documentList.getTrainingFeatures()
        X = np.zeros((len(documents), len(features)))
        Y = []
        for (r, document) in enumerate(documents):
            for (w, f) in document.getCount().getFeaturesTfidfZip():
                if w in features:
                    X[r][features.index(w)] = f
            Y.append(document.getClassInformation().getGt())
        return X, Y


    def trainData(self, X, Y):
        """
        Trains the given data.

        Arguments:
        X    ()
            --
        Y    ()
            --

        Returns:
        clf  ()
            --
        """
        clf = svm.SVC(gamma='scale', probability=True)
        clf.fit(X, Y)
        return clf


    def evaluateClassification(self, probsTest, Ytest):
        """
        Generates the values of a confusion matrix based on
        probabilities of classes and document ground truths.

        Arguments:
        probsTest  ([(float, float)])
            --
        Ytest      ([int])
            --

        Returns:
        tp   (int)
            -- the number of accurately predicted positive
               classifications
        tn   (int)
            -- the number of accurately predicted negative
               classifications
        fp   (int)
            -- the number of inaccurately predicted positive
               classifications
        fn   (int)
            -- the number of inaccurately predicted negative
               classifications
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

    def accuracy(self, tp, tn, fp, fn):
        """
        Calculates the accuracy score given a confusion matrix.

        Arguments:
        tp   (int)
            -- the number of accurately predicted positive
               classifications
        tn   (int)
            -- the number of accurately predicted negative
               classifications
        fp   (int)
            -- the number of inaccurately predicted positive
               classifications
        fn   (int)
            -- the number of inaccurately predicted negative
               classifications

        Returns:
        acc  (float)
            -- the accuracy score
        """
        acc = (tp + tn) / (tp + tn + fp + fn)
        return acc

    def balancedAccuracy(self, tp, tn, fp, fn):
        """
        Calculates the balanced accuracy score given a confusion
        matrix.

        Arguments
        tp    (int)
            -- the number of accurately predicted positive
               classifications
        tn    (int)
            -- the number of accurately predicted negative
               classifications
        fp    (int)
            -- the number of inaccurately predicted positive
               classifications
        fn    (int)
            -- the number of inaccurately predicted negative
               classifications

        Returns:
        bacc  (float)
            -- the balanced accuracy score
        """
        tpr = tp / (tp + fn)
        tnr = tn / (tn + fp)
        bacc = (tpr + tnr) / 2
        return bacc
