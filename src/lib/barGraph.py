import matplotlib.pyplot as plt
import numpy as np
import os

from lib.filesInOut import readCSVinDict
from lib.combineCSVs import collatingCSVs


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

    fig = plt.figure()
    ax = fig.add_subplot(111)

    index = np.arange(len(wordList))
    p = []
    legends = []
    bottom = np.zeros(len(wordList))
    for i in range(len(wordCountList)):
        p.append(ax.bar(index, barGraphArray[i], bottom=bottom))
        bottom += barGraphArray[i]
        legends.append(p[i][0])

    # plt.legend(legends, filenames, bbox_to_anchor=(0, 1.1, 1.0, 0), mode="expand", loc="lower left")
    plt.xlabel('Word', fontsize=8)
    plt.xticks(index, wordList, fontsize=10, rotation = 75)
    plt.ylabel('Cumulative Frequency in Documents', fontsize=8)
    plt.title(title)
    plt.tight_layout()
    return plt, fig

def barGraphGroupPath(origin, num, title):
    wordCountList = []
    filenames = []
    filePaths = []
    for file in os.listdir(origin):
        filePath = os.path.join(origin, file)
        if '.csv' in filePath:
            discard, filenameAndExt = filePath.rsplit('/', 1)
            filename, originExt = filenameAndExt.split('.')
            filenames.append(filename)
            wordCount = readCSVinDict(filePath)
            wordCountList.append(wordCount)


    if wordCountList:
            plt, fig = barGraphGroup(wordCountList, filenames, num, title)
            slashNum = origin.count('/')
            location, rest = origin.split('/', 1)
            location = 'graphs'
            name = 'graph'
            destinationExt = 'png'
            destination = '%s/%s/%s.%s' % (location, rest, name, destinationExt)
            plt.savefig(destination)
            plt.clf()
            plt.close(fig)
