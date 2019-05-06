from sklearn import svm
import numpy as np


"""

"""
class ClassificationTools:


    def formulateXY(self, documents, documentList):
        """

        """
        allFeatures = documentList.getAllFeatures()
        X = np.zeros((len(documents), len(allFeatures)))
        Y = []
        for (r, document) in enumerate(documents):
            for (w, f) in document.getCount().getFeaturesTfidfcfZip():
                X[r][allFeatures.index(w)] = f
            Y.append(document.getClassInformation().getGt())
        return X, Y


    def trainData(self, X, Y):
        """

        """
        clf = svm.SVC(gamma='scale', probability=True)
        # clf = MultinomialNB()
        clf.fit(X, Y)
        return clf


    def evaluateClassification(self, probsTest, Ytest):
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

    def accuracy(self, tp, tn, fp, fn):
        """

        """
        return (tp + tn) / (tp + tn + fp + fn)

    def balancedAccuracy(self, tp, tn, fp, fn):
        """

        """
        tpr = tp / (tp + fn)
        tnr = tn / (tn + fp)
        return (tpr + tnr) / 2
