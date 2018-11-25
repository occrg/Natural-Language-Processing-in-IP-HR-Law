import os
import csv

from lib.filesInOut import openTXTfile
from lib.filesInOut import dictToCSVfile
from lib.tokeniseTXT import splitByWord


def sortWordCount(wordCount):
    sortedWordCount = sorted(wordCount.items(), key=lambda kv: kv[1], reverse=True)
    return sortedWordCount

def countWords(words):
    wordCount = {}
    for w in words:
        if w in wordCount:
            wordCount[w] += 1
        else:
            wordCount[w] = 1
    sortedWordCount = sortWordCount(wordCount)
    return sortedWordCount


def TXTtoCSVwordCount(origin, destination):
    text = openTXTfile(origin)
    words = splitByWord(text)
    wordCount = countWords(words)
    dictToCSVfile(wordCount, destination)

def folderOfTXTsToCSVs(originFolder, destinationFolder):
    for file in os.listdir(originFolder):
        filePath = os.path.join(originFolder, file)
        filename, ext = file.split(".")
        destination = "%s/%s.csv" % (destinationFolder, filename)
        TXTtoCSVwordCount(filePath, destination)
