"""
Performs all operations for the project.

This currently consists of:
1. Converting law journal articls in PDF form into plain text format,
2. Finding the word count of every word in each article,
3. Totalling the word counts of all words for their respective classes.
"""

import os
import sys

from lib.convertpdf import pdfToString

from lib.count import stringToWordCount

from lib.combine import separateWordCountsIntoClasses
from lib.combine import combineDicts

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
    for a in areasOfLaw:
        folder = 'TXTs/%s' % a
        classLabel = a

        for path in loadListOfFilePaths(folder):
            text = txtFileToString(path)
            wordCount = stringToWordCount(text, classLabel, stopwords)
            destination =                                                     \
                changeRootFolderAndExtRemoveArea(path, 'wordCounts', 'csv')
            dictToCSVfile(wordCount, destination)

def combineIntoClasses(areasOfLaw):
    """
    Takes each csv file in 'wordCounts/' and produces a csv file in
    'wordCounts/combinations' for each item in areasOfLaw that sums the
    word count of all words occuring in documents of the respective
    class.

    Keyword arguments:
    areasOfLaw  ([str]) -- list of labels for classes
    """
    folder = 'wordCounts'
    wordCountListList = []
    wordCounts = []

    for path in loadListOfFilePaths(folder):
        wordCount = csvFileToDict(path)
        wordCounts.append(wordCount)
    wordCountListList = separateWordCountsIntoClasses(wordCounts, areasOfLaw)

    for wordCountList in wordCountListList:
        classLabel = next(iter(wordCountList[0].values()))[1]
        combined = combineDicts(wordCountList, classLabel)
        destination = '%s/combinations/%s.csv' % (folder, classLabel)
        dictToCSVfile(combined, destination)


def main():
    areasOfLaw = ['hr', 'ip']
    if(len(sys.argv) != 1):
        raise ValueError(                                                     \
        "There should be no arguments (excluding Python file name).")
    convertPDFtoTXTfiles(areasOfLaw)
    countAll(areasOfLaw)
    combineIntoClasses(areasOfLaw)


if __name__ == '__main__':
    main()
