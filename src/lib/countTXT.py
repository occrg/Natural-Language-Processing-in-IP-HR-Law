import os
import csv

from lib.filesInOut import openTXTfile
from lib.filesInOut import dictToCSVfile
from lib.tokeniseTXT import splitByWord
from lib.tokeniseTXT import lemmatisePhrases


def sortDict(dict):
    sortedDict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    return sortedDict

def countWords(words):
    wordCount = {}
    for w in words:
        if w in wordCount:
            wordCount[w] += 1
        else:
            wordCount[w] = 1
    sortedWordCount = sortDict(wordCount)
    return sortedWordCount

def countGivenPhrases(phrases, words):
    phrases = lemmatisePhrases(phrases)
    phraseCount = {}
    phrasesOnly = []
    for p in phrases:
        phraseInWords = p.split()
        for i in range(len(words)):
            phraseMatch = True
            for j in range(len(phraseInWords)):
                try:
                    if not words[i + j] == phraseInWords[j]:
                        phraseMatch = False
                except IndexError:
                    phraseMatch = False
            if phraseMatch:
                if p in phraseCount:
                    phraseCount[p] += 1
                else:
                    phraseCount[p] = 1
    sortedPhraseCount = sortDict(phraseCount)
    return sortedPhraseCount


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
