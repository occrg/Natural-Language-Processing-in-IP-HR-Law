import matplotlib.pyplot as plt
import numpy as np
import os

from lib.filesInOut import readCSVinList
from lib.filesInOut import readCSVinDict
from lib.combineCSVs import collatingCSVs

def barGraphDict(wordCount, title):
    index = np.arange(len(wordCount))
    labels = []
    frequencies = []
    for i in range(len(wordCount)):
        labels.append(wordCount[i][0])
        frequencies.append(wordCount[i][1])
    plt.bar(index, frequencies)
    plt.xlabel('Word', fontsize=8)
    plt.xticks(index, labels, fontsize=10, rotation = 75)
    plt.ylabel('Frequency of Occurrence in Documents', fontsize=8)
    plt.title(title)
    plt.tight_layout()
    return plt

def barGraphPath(origin, num, title):
    wordCount = readCSVinList(origin, num)
    plt = barGraphDict(wordCount, title)
    location, docType, area, rest = origin.split('/', 4)
    restAndFilename, ext = rest.split('.')
    location = 'graphs'
    ext = 'png'
    destination = '%s/%s/%s/%s.%s' % (location, docType, area, restAndFilename, ext)
    plt.savefig(destination)

def barGraphGroup(wordCountList, filenames, num, title):
    wordCountsCombinedLong = collatingCSVs(wordCountList)
    wordCountsCombined = wordCountsCombinedLong[:num]
    wordList = []
    for wc in wordCountsCombined:
        wordList.append(wc[0])
    barGraphArray = np.zeros((len(wordCountList), num))
    n = 0
    for sepWordCount in wordCountList:
        for row in sepWordCount:
            for w in wordList:
                if w == row:
                    barGraphArray[n][wordList.index(w)] = sepWordCount[row]
        n += 1

    index = np.arange(len(wordList))
    p = []
    legends = []
    bottom = np.zeros(len(wordList))
    for i in range(len(wordCountList)):
        p.append(plt.bar(index, barGraphArray[i], bottom=bottom))
        bottom += barGraphArray[i]
        legends.append(p[i][0])

    plt.legend(legends, filenames, bbox_to_anchor=(0, 1.1, 1.0, 0), mode="expand", loc="lower left")
    plt.xlabel('Word', fontsize=8)
    plt.xticks(index, wordList, fontsize=10, rotation = 75)
    plt.ylabel('Cumulative Frequency in Documents', fontsize=8)
    plt.title(title)
    plt.tight_layout()
    return plt

def barGraphGroupPath(origin, num, title):
    wordCountList = []
    filenames = []
    filePaths = []
    for file in os.listdir(origin):
        filePath = os.path.join(origin, file)
        discard, filenameAndExt = filePath.rsplit('/', 1)
        filename, originExt = filenameAndExt.split('.')

        if originExt == 'csv':
            filenames.append(filename)
            wordCount = readCSVinDict(filePath, num)
            wordCountList.append(wordCount)
    if wordCountList:
        plt = barGraphGroup(wordCountList, filenames, num, title)
        location, docType, area = origin.split('/', 3)
        location = 'graphs'
        name = 'graph'
        destinationExt = 'png'
        destination = '%s/%s/%s/%s.%s' % (location, docType, area, location, destinationExt)
        plt.savefig(destination)
