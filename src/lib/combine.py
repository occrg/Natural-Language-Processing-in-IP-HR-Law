"""
Supplies functionality that combines dictionaries together.
"""

import numpy as np
import random


def separateWordCountsIntoClasses(wordCounts, areasOfLaw):
    """
    Separates word counts into which class the document they represent is
    from.

    Arguments:
    wordCounts          ([{(str, str): int}])
            -- a list of dictionaries that are to be split based on the
               second tuple value of all its members' keys
    areasOfLaw          ([str])
            -- a list of areas of law that are the expected values of
               the second tuple value of each word counts' keys

    Returns:
    wordCountsListList  ([[{(str, str): int}]])
            -- a list of lists that contain dictionaries. Each list
               contains dictionaries where all its members' classes
               match an item in ${areasOfLaw}
    """
    wordCountsListList = []

    for a in areasOfLaw:
        wordCountsClass = []
        for wordCount in wordCounts:
            wordCountAllInClass = True
            for w in wordCount:
                if w[1] != a:
                    wordCountAllInClass = False
                    break
            if wordCountAllInClass:
                wordCountsClass.append(wordCount)
        wordCountsListList.append(wordCountsClass)
    return wordCountsListList

def combineDicts(wordCounts):
    """
    Adds all the values with the same key across a list of word counts.

    Arguments:
    wordCounts            ([{(str, str): int}])
            -- a list of dictionaries that's elements are to be
               combined by adding their values if they have the same
               key

    Returns:
    wordCountWithClasses  ([{(str, str): int}])
            -- a dictionary that contains the combined dictionaries
    """
    wordCounts = {}
    for wc in wordCounts:
        for row in wc:
            if row in wordCounts.keys():
                wordCounts[row] = wordCounts[row] + wc[row]
            else:
                wordCounts[row] = wc[row]
    return wordCounts

def allWords(wordCounts):
    """
    Compiles a list of words used in ${wordCounts}.

    Arguments:
    wordCounts  ([{(str, str): int}])
            -- a list of dictionaries that's words are to be compiled

    Returns:
    words       ([str])
            -- a list of strings that each represent a word from
               ${wordCounts}
    """
    words = []
    for wc in wordCounts:
        for row in wc:
            if row[0] not in words:
                words.append(row[0])
    return words

def fillWordCounts(wordCounts):
    """
    Converts dictionaries into a matrix form that is accepted by
    scikitlearn.

    This is a matrix where a row represents a document and each column
    represents a different feature. The columns include all features
    contained in all documents.

    Arguments:
    wordCounts  ([{(str, str): int}])
                -- a list of dictionaries that's words are to be compiled

    counts      (ndarray)
                -- a matrix with each row representing a sample (a
                   dictionary in ${wordCounts}) and each column
                   representing a different feature
    """
    words = allWords(wordCounts)

    counts = np.zeros((len(wordCounts), len(words)))

    wcInd = 0
    for wc in wordCounts:
        for row in wc:
            if row[0] in words:
                counts[wcInd][words.index(row[0])] = wc[row]
        wcInd += 1
    return counts

def getTruths(wordCounts):
    """
    Extracts the class of a document, with 'hr' represented by 0 and
    'ip' represented by 1.

    Arguments:
    wordCounts  ([{(str, str): (int)}])
            -- a list of dictionaries that's class are to be extracted.
               In the dictionary, this is represented by the second
               tuple value of the key

    Returns:
    Y  ([int])
            -- a list of integers: [0,1]. The ith element represents
               the class of the ith word count in ${wordCounts} with
               'hr' represented by 0 and 'ip' represented by 1
    """
    Y = []
    for wc in wordCounts:
        if next(iter(wc.keys()))[1] == 'hr':
            Y.append(0)
        else:
            Y.append(1)
    return Y

def splitTestAndTrain(X, Y, propTrain):
    """
    Splits the given data into two datasets randomly.

    Arguments:
    X          (ndarray) -- the features of the entire dataset to be
                            split
    Y          ([int])   -- the classes of each sample of the entire
                            dataset to be split
    propTrain  (float)   -- a float between 0 and 1 that represents the
                            proportion of the dataset that is to be
                            trained on

    Returns:
    Xtrain     (ndarray) -- the portion of X that is to be trained on
    Ytrain     ([int])   -- the portion of Y that is to be trained on
    Xtest      (ndarray) -- the portion of X that will be tested
    Ytest      ([int])   -- the portion of Y that the tests on ${Xtest}
                            will be checked against
    """
    trainNum = round(len(Y) * propTrain)
    testNum = len(Y) - trainNum
    testIndexes = []
    indexes = list(range(len(Y)))
    trainIndexes = indexes
    for i in range(testNum):
        randElement = random.choice(indexes)
        trainIndexes.remove(randElement)
        testIndexes.append(randElement)
    Xtrain = np.zeros((trainNum, X.shape[1]))
    Ytrain = []
    Xtest = np.zeros((testNum, X.shape[1]))
    Ytest = []

    for i in range(trainNum):
        Xtrain[i] = X[trainIndexes[i]]
        Ytrain.append(Y[trainIndexes[i]])

    for i in range(testNum):
        Xtest[i] = X[testIndexes[i]]
        Ytest.append(Y[testIndexes[i]])
    return Xtrain, Ytrain, Xtest, Ytest
