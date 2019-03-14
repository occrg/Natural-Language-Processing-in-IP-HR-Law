"""
Performs all operations for the project.

This currently consists of:
1. Converting law journal articls in PDF form into plain text format,
2. Finding the word count of every word in each article,
3. Totalling the word counts of all words for their respective classes
   and normalising these counts to make them more appropriate features,
4. Training and testing the gathered data,
5. Visualising the test data.
"""

import os
import sys
import numpy as np
import datetime
import matplotlib
import matplotlib.pyplot as plt

from lib.convertpdf import pdfToString
from lib.convertpdf import getPDFmetadata

from lib.count import stringToWordCount

from lib.tokenise import splitBySentence

from lib.filter import removeSentencesWithoutPhrases

from lib.frequencies import tfidf

from lib.restructure import getListFromDocumentDetails
from lib.restructure import allWords
from lib.restructure import fillWordCounts
from lib.restructure import getTruths
from lib.restructure import allocateTestAndTrain
from lib.restructure import filterDocuments

from lib.classification import trainData
from lib.classification import testData

from lib.visualisation import plot

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
    Converts all PDFs in './data/pdf/${areasOfLaw}/' to plaintext and
    stores in txt files in '/data/txt/'.

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

                details = {'title':title, 'pdfPath':path,                    \
                    'txtPath':destination, 'countPath':'',                   \
                    'frequencyPath':'', 'date':date, 'class':classLabel,     \
                    'test':0, 'hrProb':-1.0, 'ipProb':-1.0, 'userProb':-1.0, \
                    'creatorProb':-1.0}

                documentDetails.append(details)

    for details in documentDetails:
        if details['pdfPath'] not in pdfFilePaths:
            documentDetails.remove(details)

    return documentDetails


def counting(documentDetails, scope):
    """
    Takes each txt file specified in ${documentDetails} and produces a
    corresponding csv file in './data/count' which contains a row for
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


def frequencyWeighting(documentDetails):
    """
    Takes each csv file specified in ${documentDetails} and converts
    the term count to some weighted frequency and then stores it as a
    csv file in './data/frequency'.

    Arguments:
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document
    """
    wordCounts = []
    for details in documentDetails:
        wordCount = csvFileToCount(details['countPath'])
        destination = changeRootFolderAndExtRemoveArea(details['countPath'], \
            'frequency', 'csv')
        details['frequencyPath'] = destination
        wordCounts.append(wordCount)

    tfidfWordCounts = tfidf(wordCounts)


    i = 0
    for wordCount in tfidfWordCounts:
        countToCSVfile(wordCount, documentDetails[i]['frequencyPath'])
        i += 1

def userCreatorRatings(documentDetails):
    """

    """
    creatorPhrases = loadPhrases('data/lists/Creator-keyPhrases.txt')
    userPhrases = loadPhrases('data/lists/User-keyPhrases.txt')
    for details in documentDetails:
        text = txtFileToString(details['txtPath'])
        sentences = splitBySentence(text)
        creatorSentences = removeSentencesWithoutPhrases(creatorPhrases, sentences)
        userSentences = removeSentencesWithoutPhrases(userPhrases, sentences)
        creatorProp = len(creatorSentences) / len(sentences)
        userProp = len(userSentences) / len(sentences)
        details['userProb'] = userProp
        details['creatorProb'] = creatorProp
    return documentDetails

def classifications(documentDetails):
    """
    Takes each csv file specified in ${documentDetails} and trains on
    some proportion of the files with regards to HR-IP and then tests
    on the rest.

    Arguments:
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document
    """
    documentDetails = allocateTestAndTrain(0.25, documentDetails)
    wordCounts = []
    for details in documentDetails:
        wordCount = csvFileToCount(details['countPath'])
        wordCounts.append(wordCount)
    words = allWords(wordCounts)

    trainDocumentDetails = filterDocuments('test', 0, documentDetails)
    trainWordCounts = []
    for details in trainDocumentDetails:
        wordCount = csvFileToCount(details['countPath'])
        trainWordCounts.append(wordCount)
    Xtrain = fillWordCounts(trainWordCounts, words)
    Ytrain = getTruths(trainDocumentDetails)
    clf = trainData(Xtrain, Ytrain)

    testDocumentDetails = filterDocuments('test', 1, documentDetails)
    testWordCounts = []
    for details in testDocumentDetails:
        wordCount = csvFileToCount(details['countPath'])
        testWordCounts.append(wordCount)
    Xtest = fillWordCounts(testWordCounts, words)
    Ytest = getTruths(testDocumentDetails)
    documentDetails = testData(clf, Xtest, Ytest, documentDetails)

    return documentDetails

def visualisations(documentDetails):
    """
    Visualises the test data with the date of document creation as the
    x-axis and the probability that a document is from an intellectual
    property journal subtracted by the probability that it is from a
    human rights document.

    Arguments:
    documentDetails  ([{}])
            -- a list of dictionaries with each dictionary giving the
               attributes of a different document
    """
    testDocumentDetails = filterDocuments('test', 1, documentDetails)
    hrTestDocumentDetails = filterDocuments('class', 0, testDocumentDetails)
    ipTestDocumentDetails = filterDocuments('class', 1, testDocumentDetails)

    hrProbsHR = np.asarray(getListFromDocumentDetails('hrProb', hrTestDocumentDetails), dtype=np.float32)
    ipProbsHR = np.asarray(getListFromDocumentDetails('ipProb', hrTestDocumentDetails), dtype=np.float32)
    userProbsHR = np.asarray(getListFromDocumentDetails('userProb', hrTestDocumentDetails), dtype=np.float32)
    creatorProbsHR = np.asarray(getListFromDocumentDetails('creatorProb', hrTestDocumentDetails), dtype=np.float32)
    datesHR = getListFromDocumentDetails('date', hrTestDocumentDetails)
    Xhr = matplotlib.dates.date2num(datesHR)
    Yhr = ipProbsHR - hrProbsHR
    Zhr = creatorProbsHR - userProbsHR

    hrProbsIP = np.asarray(getListFromDocumentDetails('hrProb', ipTestDocumentDetails), dtype=np.float32)
    ipProbsIP = np.asarray(getListFromDocumentDetails('ipProb', ipTestDocumentDetails), dtype=np.float32)
    userProbsIP = np.asarray(getListFromDocumentDetails('userProb', ipTestDocumentDetails), dtype=np.float32)
    creatorProbsIP = np.asarray(getListFromDocumentDetails('creatorProb', ipTestDocumentDetails), dtype=np.float32)
    datesIP = getListFromDocumentDetails('date', ipTestDocumentDetails)
    Xip = matplotlib.dates.date2num(datesIP)
    Yip = ipProbsIP - hrProbsIP
    Zip = creatorProbsIP - userProbsIP


    Xs = []
    Ys = []
    Zs = []
    Cs = []
    Xs.append(Xhr)
    Xs.append(Xip)
    Ys.append(Yhr)
    Ys.append(Yip)
    Zs.append(Zhr)
    Zs.append(Zip)
    Cs.append('r')
    Cs.append('b')

    plot(Xs, Ys, Zs, Cs)


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
    documentDetails = convertingPDFs(areasOfLaw, documentDetails, 'new')
    documentDetails = counting(documentDetails, 'new')
    documentDetials = frequencyWeighting(documentDetails)
    documentDetails = classifications(documentDetails)
    documentDetails = userCreatorRatings(documentDetails)
    documentDetailsToCSVfile(documentDetails, path)
    visualisations(documentDetails)


if __name__ == '__main__':
    main()
