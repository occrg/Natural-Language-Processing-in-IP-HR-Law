import sys
import os
from lib.filesInOut import loadPhrases
from lib.countTXT import folderOfTXTsToCSVs
from lib.countTXT import folderOfTXTsToPhrasesCSVs
from lib.combineCSVs import folderToCombined
from lib.barGraph import barGraphPath
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

def graphAllCounts(typesOfDocument, areasOfLaw):
    originFolder = 'wordCounts'
    numberOfTopResults = 20
    for t in typesOfDocument:
        for a in areasOfLaw:
            originFolderPath = '%s/%s/%s' % (originFolder, t, a)
            for file in os.listdir(originFolderPath):
                filePath = os.path.join(originFolderPath, file)
                if '.' in filePath:
                    barGraphPath(filePath, numberOfTopResults, originFolderPath)

def combinedCountGraphs(typesOfDocument, areasOfLaw):
    originFolder = 'wordCounts'
    numberOfTopResults = 20
    for t in typesOfDocument:
        for a in areasOfLaw:
            originFolderPath = '%s/%s/%s' % (originFolder, t, a)
            barGraphGroupPath(originFolderPath, numberOfTopResults, originFolderPath)


def localToPhraseWordCountAll(typesOfDocument, areasOfLaw):
    a = 0


def main():
    typesOfDocument = ['journals', 'treaties']
    areasOfLaw = ['hr', 'ip']
    if(len(sys.argv) != 1):
        raise ValueError("There should be no arguments (excluding Python file name).")
    countAll(typesOfDocument, areasOfLaw)
    # combineAllCounts(typesOfDocument, areasOfLaw)
    # graphAllCounts(typesOfDocument, areasOfLaw)
    combinedCountGraphs(typesOfDocument, areasOfLaw)
    phraseCountAll(typesOfDocument, areasOfLaw)

if __name__ == '__main__':
    main()
