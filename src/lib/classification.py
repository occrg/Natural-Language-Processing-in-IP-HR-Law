"""
Supplies functionality for the training and testing of the model.
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
import numpy as np
from sklearn.model_selection import cross_val_score


def trainData(X, Y):
    """
    Trains a model based on data ${X} and ground truths ${Y}.

    Arguments:
    X  (ndarray) -- the matrix of training data with each row
                    representing a different document and each column
                    representing a different feature
    Y  ([int])   -- the array of classes with the ith item, giving the
                    class of the document on the ith row of ${X}

    Returns:
    clf (SVC)    -- a model that has been trained on ${X} and ${Y}
    """
    clf = svm.SVC(gamma='scale', probability=True)
    clf.fit(X, Y)
    return clf

def testData(clf, X, Y, documentDetails):
    """
    Tests the ${clf} model using samples ${X} against its ground truths
    ${Y} and then updates documentDetails to reflect the probability
    that each document falls into a class.

    Arguments:
    clf              (model)
            -- the model that is to be evaluated
    X                (ndarray)
            -- the matrix of test data with each row representing a
               different document and each column representing a
               different feature
    Y                ([int])
            -- the array of classes with the ith item, giving the
               class of the document on the ith row of ${Y}
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document

    Returns:
    documentDetails  ([{}])
            -- the same list of dictionaries but with the propbability
               of each document falling into each class added
    """
    probabilities = clf.predict_proba(X)
    success = clf.score(X, Y)
    i = 0
    for details in documentDetails:
        if details['test']:
            details['hrProb'] = probabilities[i][0]
            details['ipProb'] = probabilities[i][1]
            i += 1
    return documentDetails
