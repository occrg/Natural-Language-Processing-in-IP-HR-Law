import os
import csv

from lib.filesInOut import openTXTfile
from lib.filesInOut import dictToCSVfile
from lib.tokeniseTXT import splitByWord
from lib.tokeniseTXT import lemmatisePhrases
from lib.tokeniseTXT import TXTtoWordList
from lib.filter import onlyWordsInSentencesContaining


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
        if p not in phraseCount:
            phraseCount[p] = 0
    sortedPhraseCount = sortDict(phraseCount)
    return sortedPhraseCount

def TXTtoCSVwordCount(origin, destination):
    words = TXTtoWordList(origin)
    wordCount = countWords(words)
    dictToCSVfile(wordCount, destination)

def TXTtoLocalToPhraseCSVcount(origin, destination, phrases):
    text = openTXTfile(origin)
    filteredWords = onlyWordsInSentencesContaining(phrases, text)
    wordCount = countWords(filteredWords)
    dictToCSVfile(wordCount, destination)

def folderOfTXTsToCSVs(originFolder, destinationFolder):
    for file in os.listdir(originFolder):
        filePath = os.path.join(originFolder, file)
        filename, ext = file.split(".")
        destination = "%s/%s.csv" % (destinationFolder, filename)
        TXTtoCSVwordCount(filePath, destination)

def folderOfTXTsToPhrasesCSVs(originFolder, destinationFolder, phrases):
    for file in os.listdir(originFolder):
        filePath = os.path.join(originFolder, file)
        filename, ext = file.split(".")
        destination = "%s/%s-phrases.csv" % (destinationFolder, filename)
        words = TXTtoWordList(filePath)
        phraseCount = countGivenPhrases(phrases, words)
        dictToCSVfile(phraseCount, destination)

def folderOfTXTsToLocalToPhrasesCSVs(originFolder, destinationFolder, phrases, category):
    for file in os.listdir(originFolder):
        filePath = os.path.join(originFolder, file)
        filename, ext = file.split(".")
        destination = "%s/%s/%s.csv" % (destinationFolder, category, filename)
        TXTtoLocalToPhraseCSVcount(filePath, destination, phrases)
