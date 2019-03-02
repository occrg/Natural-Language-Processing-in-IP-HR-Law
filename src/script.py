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

from lib.count import stringToWordCount

from lib.combine import separateWordCountsIntoClasses
from lib.combine import combineDicts
from lib.combine import fillWordCounts
from lib.combine import getTruths
from lib.combine import splitTestAndTrain

from lib.classification import trainData

from lib.filepaths import loadListOfFilePaths
from lib.filepaths import changeRootFolderAndExt
from lib.filepaths import changeRootFolderAndExtRemoveArea

from lib.filesio import csvFileToDict
from lib.filesio import stringToTXTfile
from lib.filesio import txtFileToString
from lib.filesio import dictToCSVfile
from lib.filesio import loadPhrases


def convertPDFtoTXTfiles(areasOfLaw):
    """
    Converts all PDFs contained in 'PDFs/${areasOfLaw}/' to txt file in
    'TXTs/${areasOfLaw}/'.

    Keyword arguments:
    areasOfLaw  ([str]) -- list of labels for classes
    """
    for a in areasOfLaw:
        folder = 'PDFs/%s' % a
        for path in loadListOfFilePaths(folder):
            text = pdfToString(path)
            destination = changeRootFolderAndExt(path, 'TXTs', 'txt')
            stringToTXTfile(text, destination)

def countAll(areasOfLaw):
    """
    Takes each txt file in 'TXTs/${areasOfLaw}/' and produces a
    corresponding csv file in 'wordCounts/' which contains a row for
    each unique word in the document, followed by the frequency of that
    word's appearance in the document, followed by the class of the
    document.

    Keyword arguments:
    areasOfLaw  ([str]) -- list of labels for classes
    """
    stopwords = loadPhrases('lists/stopwords.txt')
    stopstrings = loadPhrases('lists/stopstrings.txt')
    for a in areasOfLaw:
        folder = 'TXTs/%s' % a
        classLabel = a

        for path in loadListOfFilePaths(folder):
            text = txtFileToString(path)
            wordCount = stringToWordCount(text, classLabel, stopwords,        \
                stopstrings)
            destination =                                                     \
                changeRootFolderAndExtRemoveArea(path, 'wordCounts', 'csv')
            dictToCSVfile(wordCount, destination)

def combineTrainingData(areasOfLaw):
    """
    Takes each csv file in 'wordCounts/' and produces a csv file in
    'wordCounts/combinations' for each item in areasOfLaw that sums the
    word count of all words occuring in documents of the respective
    class. It also creates a file
    'wordCounts/combinations/combination.csv' which consists of all
    word counts combined.

    Keyword arguments:
    areasOfLaw  ([str]) -- list of labels for classes
    """
    wordCountListList = []
    wordCounts = []

    for path in loadListOfFilePaths('wordCounts'):
        wordCount = csvFileToDict(path)
        wordCounts.append(wordCount)

    wordCountListList = separateWordCountsIntoClasses(wordCounts, areasOfLaw)

    for wordCountList in wordCountListList:
        classLabel = next(iter(wordCountList[0].keys()))[1]
        combined = combineDictsSameClass(wordCountList, classLabel)
        destination = 'wordCounts/combinations/%s.csv' % classLabel
        dictToCSVfile(combined, destination)

    combined = combineDicts(wordCounts)
    destination = 'wordCounts/combinations/combined.csv'
    dictToCSVfile(combined, destination)


def performClassification():
    """
    Takes each csv file in 'wordCounts/' and trains on some proportion
    of the files and then tests on the rest.
    """
    wordCounts = []

    for path in loadListOfFilePaths('wordCounts'):
        wordCount = csvFileToDict(path)
        wordCounts.append(wordCount)

    X = fillWordCounts(wordCounts)
    y = getTruths(wordCounts)
    Xtrain, Ytrain, Xtest, Ytest = splitTestAndTrain(X, y, 0.75)

    clf = trainData(Xtrain, Ytrain)
    results = clf.predict_proba(Xtest)
    print(results)
    print(clf.score(Xtest, Ytest))



def main():
    areasOfLaw = ['hr', 'ip']
    if(len(sys.argv) != 1):
        raise ValueError(                                                     \
        "There should be no arguments (excluding Python file name).")
    # convertPDFtoTXTfiles(areasOfLaw)
    # countAll(areasOfLaw)
    # combineTrainingData(areasOfLaw)
    performClassification()


if __name__ == '__main__':
    main()
