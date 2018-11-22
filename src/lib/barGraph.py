import matplotlib.pyplot as plt
import numpy as np
import os

def readCSVordered(origin, num):
    if(not os.path.isfile(origin)):
        raise ValueError("File does not exist. File path (%s) wrong." % path)
    file = open('%s' % origin, 'r')
    wordCount = {}
    index = 0
    for line in file.readlines()[:num]:
        key, rhs = line.split(",")
        value = int(rhs)
        wordCount[index] = (key, value)
        index += 1
        file.close()
    return wordCount

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
    wordCount = readCSVordered(origin, num)
    plt = barGraphDict(wordCount, title)
    directories = origin.count('/')
    location, docType, area, rest = origin.split('/', 4)
    restAndFilename, ext = rest.split('.')
    location = 'graphs'
    ext = 'png'
    destination = '%s/%s/%s/%s.%s' % (location, docType, area, restAndFilename, ext)
    plt.savefig(destination)
