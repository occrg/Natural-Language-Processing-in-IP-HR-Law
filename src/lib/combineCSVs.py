import sys
import os
import csv

from lib.filesInOut import readCSVinDict
from lib.filesInOut import dictToCSVfile


def sortWordCount(wordCount):
    sortedWordCount = sorted(wordCount.items(), key=lambda kv: kv[1], reverse=True)
    return sortedWordCount

def collatingCSVs(wordCountsList):
    wordCounts = {}
    alreadyInDict = []
    for wc in wordCountsList:
        for row in wc:
            if row in wordCounts.keys():
                wordCounts[row] = wordCounts[row] + wc[row]
                alreadyInDict.append(row)
            else:
                wordCounts[row] = wc[row]
    wordCounts = sortWordCount(wordCounts)
    return wordCounts

def combiningCSVsFromPaths(filePaths):
    wordCountsList = []
    for p in filePaths:
        numLines = sum(1 for line in open(p))
        currWordCount = readCSVinDict(p)[:numLines]
        wordCountsList.append(currWordCount)
    wordCounts = collatingCSVs(wordCountsList)
    return wordCounts


def folderToCombined(folder):
    if os.listdir(folder):
        destination = '%s/combination.csv' % folder
        if os.path.isfile(destination):
            os.remove(destination)
        filePaths = []
        for file in os.listdir(folder):
            currWordCount = {}
            alreadyInDict = []
            filePath = os.path.join(folder, file)
            if '.' in filePath:
                filePaths.append(filePath)
        wordCounts = combiningCSVsFromPaths(filePaths)
        dictToCSVfile(wordCounts, destination)
