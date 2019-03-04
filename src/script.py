"""
Performs all operations for the project.

This currently consists of:
1. Converting law journal articls in PDF form into plain text format,
2. Finding the word count of every word in each article,
3. Totalling the word counts of all words for their respective classes,
4. Training and testing the gathered data.
"""

import os
import sys
import numpy as np

from lib.convertpdf import pdfToString
from lib.convertpdf import getPDFmetadata

from lib.count import stringToWordCount

from lib.restructure import getListFromDocumentDetails
from lib.restructure import fillWordCounts
from lib.restructure import getTruths
from lib.restructure import splitTestAndTrain

from lib.classification import trainData
from lib.classification import testData

from lib.filepaths import loadListOfFilePaths
from lib.filepaths import changeRootFolderAndExtRemoveArea

from lib.filesio import csvFileToCount
from lib.filesio import stringToTXTfile
from lib.filesio import txtFileToString
from lib.filesio import countToCSVfile
from lib.filesio import csvFileToDocumentDetails
from lib.filesio import documentDetailsToCSVfile
from lib.filesio import loadPhrases


def convertingPDFs(areasOfLaw, documentDetails, scope):
    """
    Converts all PDFs in 'data/pdf/${areasOfLaw}/' to plaintext and
    stores in txt files in 'data/txt/'.

    Arguments:
    areasOfLaw       ([str])
            -- list of labels for classes
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document
    scope            str
            -- a string with the value of either 'new' or 'all'. If
               'new' then the function will only convert PDFs that have
               not already been converted. If 'all', the function will
               convert regardless and overwrite current txt files
    """
    if scope == 'all':
        documentDetails = []

    alreadyConverted = getListFromDocumentDetails('txtPath', documentDetails)
    pdfFilePaths = []

    for a in areasOfLaw:
        folder = 'data/pdf/%s' % a
        for path in loadListOfFilePaths(folder):
            pdfFilePaths.append(path)
            destination = changeRootFolderAndExtRemoveArea(path, 'txt', 'txt')
            if destination not in alreadyConverted:
                text = pdfToString(path)
                date, title = getPDFmetadata(path)
                stringToTXTfile(text, destination)
                if a == 'hr':
                    classLabel = 0
                if a == 'ip':
                    classLabel = 1

                details = {'title':title, 'pdfPath':path, 'txtPath':destination, \
                    'countPath':'', 'date':date, 'class':classLabel, 'test':0,   \
                    'hrProb':-1.0, 'ipProb':-1.0, 'userProb':-1.0,               \
                    'creatorProb':-1.0}

                documentDetails.append(details)

    for details in documentDetails:
        if details['pdfPath'] not in pdfFilePaths:
            documentDetails.remove(details)

    return documentDetails

def counting(documentDetails, scope):
    """
    Takes each txt file specified in ${documentDetails} and produces a
    corresponding csv file in 'wordCounts/' which contains a row for
    each unique word in the document, followed by the frequency of that
    word's appearance in the document.

    Arguments:
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document
    scope            str
            -- a string with the value of either 'new' or 'all'. If
               'new' then the function will only convert PDFs that have
               not already been converted. If 'all', the function will
               convert regardless and overwrite current txt files
    """
    stopwords = loadPhrases('data/lists/stopwords.txt')
    stopstrings = loadPhrases('data/lists/stopstrings.txt')
    for details in documentDetails:
        if details['countPath'] == '' or scope == 'all':
            text = txtFileToString(details['txtPath'])
            wordCount = stringToWordCount(text, stopwords, stopstrings)
            destination = changeRootFolderAndExtRemoveArea(                      \
                details['txtPath'], 'count', 'csv')
            countToCSVfile(wordCount, destination)
            details['countPath'] = destination
    return documentDetails

def classifications(documentDetails):
    """
    Takes each csv file specified in ${documentDetails} and trains on
    some proportion of the files and then tests on the rest.

    Arguments:
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document
    """
    wordCounts = []

    for details in documentDetails:
        wordCount = csvFileToCount(details['countPath'])
        wordCounts.append(wordCount)

    X = fillWordCounts(wordCounts)
    Y = getTruths(documentDetails)

    documentDetails, Xtrain, Ytrain, Xtest, Ytest =                         \
        splitTestAndTrain(X, Y, 0.75, documentDetails)

    clf = trainData(Xtrain, Ytrain)
    documentDetails = testData(clf, Xtest, Ytest, documentDetails)
    return documentDetails


def main():
    areasOfLaw = ['hr', 'ip']
    if(len(sys.argv) != 1):
        raise ValueError(                                                     \
            "There should be no arguments (excluding Python file name).")
    path = 'data/documentDetails.csv'
    if os.path.isfile(path):
        documentDetails = csvFileToDocumentDetails(path)
    else:
        documentDetails = []
    documentDetails = convertingPDFs(areasOfLaw, documentDetails, 'all')
    documentDetails = counting(documentDetails, 'all')
    documentDetails = classifications(documentDetails)
    documentDetailsToCSVfile(documentDetails, path)


if __name__ == '__main__':
    main()
