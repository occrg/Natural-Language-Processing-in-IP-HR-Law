import sys
import os
from lib.filesInOut import loadPhrases
from lib.countTXT import folderOfTXTsToCSVs
from lib.countTXT import folderOfTXTsToPhrasesCSVs
from lib.countTXT import folderOfTXTsToLocalToPhrasesCSVs
from lib.combineCSVs import folderToCombined
from lib.barGraph import barGraphGroupPath
from lib.tokeniseTXT import folderOfTXTsToWordLists


def countAll(typesOfDocument, areasOfLaw):
    originFolder = 'TXTs'
    destinationFolder = 'wordCounts'
    for t in typesOfDocument:
        for a in areasOfLaw:
            origin = '%s/%s/%s' % (originFolder, t, a)
            destination = '%s/%s/%s' % (destinationFolder, t, a)
            folderOfTXTsToCSVs(origin, destination)

def phraseCountAll(typesOfDocument, areasOfLaw):
    originFolder = 'TXTs'
    destinationFolder = 'wordCounts'
    insideFolder = 'phrases'
    phrases = loadPhrases('lists/keyPhrases.txt')
    for t in typesOfDocument:
        for a in areasOfLaw:
            origin = '%s/%s/%s' % (originFolder, t, a)
            destination = '%s/%s/%s/%s' % (destinationFolder, t, a, insideFolder)
            folderOfTXTsToPhrasesCSVs(origin, destination, phrases)

def combineAllCounts(typesOfDocument, areasOfLaw):
    originFolder = 'wordCounts'
    for t in typesOfDocument:
        for a in areasOfLaw:
            origin = '%s/%s/%s' % (originFolder, t, a)
            folderToCombined(origin)


def combinedCountGraphs(typesOfDocument, areasOfLaw):
    originFolder = 'wordCounts'
    phrasesLocs = ['HR', 'IP', 'User', 'Creator']
    numberOfTopResults = 20
    for t in typesOfDocument:
        for a in areasOfLaw:
            originFolderPath = '%s/%s/%s' % (originFolder, t, a)
            barGraphGroupPath(originFolderPath, numberOfTopResults, originFolderPath)
            originFolderPath = '%s/%s/%s/phrases' % (originFolder, t, a)
            barGraphGroupPath(originFolderPath, numberOfTopResults, originFolderPath)
            for p in phrasesLocs:
                originFolderPath = '%s/%s/%s/phrases-local/%s' % (originFolder, t, a, p)
                barGraphGroupPath(originFolderPath, numberOfTopResults, originFolderPath)



def localToPhraseWordCountAll(typesOfDocument, areasOfLaw):
    originFolder = 'TXTs'
    destinationFolder = 'wordCounts'
    insideFolder = 'phrases-local'
    phrasesLocs = ['HR', 'IP', 'User', 'Creator']
    phrases = loadPhrases('lists/keyPhrases.txt')
    for t in typesOfDocument:
        for a in areasOfLaw:
            origin = '%s/%s/%s' % (originFolder, t, a)
            destination = '%s/%s/%s/%s' % (destinationFolder, t, a, insideFolder)
            for p in phrasesLocs:
                phrases = loadPhrases('lists/%s-keyPhrases.txt' % p)
                folderOfTXTsToLocalToPhrasesCSVs(origin, destination, phrases, p)


def main():
    typesOfDocument = ['journals', 'treaties']
    areasOfLaw = ['hr', 'ip']
    if(len(sys.argv) != 1):
        raise ValueError("There should be no arguments (excluding Python file name).")
    countAll(typesOfDocument, areasOfLaw)
    # combineAllCounts(typesOfDocument, areasOfLaw)
    phraseCountAll(typesOfDocument, areasOfLaw)
    localToPhraseWordCountAll(typesOfDocument, areasOfLaw)
    combinedCountGraphs(typesOfDocument, areasOfLaw)

if __name__ == '__main__':
    main()
