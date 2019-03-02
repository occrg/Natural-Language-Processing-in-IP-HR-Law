from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
import numpy as np
from sklearn.model_selection import cross_val_score


def trainData(X, Y):
    """
    Trains a model based on data ${X}.

    Arguments:
    X  (ndarray) -- the matrix of training data with each row
                    representing a different document and ech column
                    representing a different feature
    Y  ([int])   -- the array of classes with the ith item, giving the
                    class of the document on the ith row of ${X}

    Returns:
    clf (SVC)    -- a model that has been trained on ${X} and ${Y}
    """
    clf = svm.SVC(gamma='scale', probability=True)
    clf.fit(X, Y)
    return clf
