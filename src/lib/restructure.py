"""
Supplies functionality that changes the format or type of data.
"""

import numpy as np
import random


def getListFromDocumentDetails(key, documentDetails):
    """
    Gets a list of all the items in ${documentDetails} with key ${key}.

    Arguments:
    key              (str)
            -- the key that's values are to be retrieved
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document

    Returns:
    items            ([any])
            -- the list of items with key ${key}
    """
    items = []
    for details in documentDetails:
        items.append(details[key])
    return items

def setListFromDocumentDetails(key, value, documentDetails):
    """
    Changes all the items in ${documentDetails} with key ${key}
    to value ${value}.

    Arguments:
    key              (str)
            -- the key that needs all its values changed
    value            (any)
            -- the value that the keys are to be set to
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document

    Returns:
    documentDetails  ([{}])
            -- the list of dictionaries with all items' values under
               key ${key} changed to ${value}
    """
    for details in documentDetails:
        details[key] = value
    return documentDetails

def allWords(wordCounts):
    """
    Compiles a list of words used in ${wordCounts}.

    Arguments:
    wordCounts  ([{str: int}])
            -- a list of dictionaries that's words are to be compiled

    Returns:
    words       ([str])
            -- a list of strings that each represent a word from
               ${wordCounts}
    """
    words = []
    for wc in wordCounts:
        for row in wc:
            if row not in words:
                words.append(row)
    return words

def fillWordCounts(wordCounts):
    """
    Converts dictionaries into a matrix form that is accepted by
    scikitlearn.

    This is a matrix where a row represents a document and each column
    represents a different feature. The columns include all features
    contained in all documents.

    Arguments:
    wordCounts  ([{str: int}])
                -- a list of dictionaries where each dictionary has a
                   set of words as keys with the counts of those words
                   as the values

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
            if row in words:
                counts[wcInd][words.index(row)] = wc[row]
        wcInd += 1
    return counts

def getTruths(documentDetails):
    """
    Extracts the class of the documents in ${documentDetails} as an
    ordered list, with 'hr' represented by 0 and 'ip' represented by 1.

    Arguments:
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document

    Returns:
    Y                ([int])
            -- a list of integers: [0,1]. The ith element represents
               the class of the ith word count in ${wordCounts} with
               'hr' represented by 0 and 'ip' represented by 1
    """
    Y = []
    for details in documentDetails:
        Y.append(details['class'])
    return Y

def allocateTestAndTrain(propTest, documentDetails):
    """
    Splits the given data into two datasets randomly and changes the
    'test' field in the appropriate ${documentDetails} items to
    reflect the split.

    Arguments:
    propTrain        (float)
            -- a float between 0 and 1 that represents the proportion
               of the dataset that is to be trained on
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document

    Returns:
    documentDetails  ([{}])
            -- the list of dictionaries with the appropriate
               dictionaries' 'test' field ammended
    """
    documentDetails =                                                        \
        setListFromDocumentDetails('test', 0, documentDetails)
    documentDetails =                                                        \
        setListFromDocumentDetails('hrProb', -1, documentDetails)
    documentDetails =                                                        \
        setListFromDocumentDetails('ipProb', -1, documentDetails)

    testNum = round(len(documentDetails) * propTest)
    for i in range(testNum):
        documentDetails[random.randint(0, len(documentDetails) - 1)]['test'] = 1
    return documentDetails

def filterDocuments(key, value, documentDetails):
    """
    Removes any items from ${documentDetails} that do not have the
    value ${value} at key ${key}.

    Arguments:
    key                      (str)
            -- the key that should have ${value} to avoid removeal
    value                    (any)
            -- the value that the remaining items will have at ${key}
    documentDetails          ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document

    Returns:
    documentDetailsFiltered  ([{}])
            -- the list of dictionaries without the dictionaries that
               did not have value ${value} at key ${key}
    """
    documentDetailsFiltered = []
    for details in documentDetails:
        if details[key] == value:
            documentDetailsFiltered.append(details)
    return documentDetailsFiltered
