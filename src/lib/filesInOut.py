import os
import csv

def loadPhrases(location):
    file = open('%s' % location, 'r')
    phrases = []
    for line in file.readlines():
        newline = line.replace('\n', '')
        phrases.append(newline)
    file.close()
    return phrases

def readCSVinList(origin, num):
    if(not os.path.isfile(origin)):
        raise ValueError("File does not exist. File path (%s) wrong." % path)
    file = open('%s' % origin, 'r')
    wordCount = []
    for line in file.readlines()[:num]:
        key, rhs = line.split(",")
        value = int(rhs)
        row = (key, value)
        wordCount.append(row)
        file.close()
    return wordCount

def readCSVinDict(path, num):
    if(not os.path.isfile(path)):
        raise ValueError("File does not exist. File path (%s) wrong." % path)
    file = open('%s' % path, 'r')
    wordCount = {}
    for line in file.readlines()[:num]:
        index, rhs = line.split(",")
        value = int(rhs)
        wordCount[index] = value
        file.close()
    return wordCount

def openTXTfile(path):
    file = open('%s' % path, 'r')
    lines = []
    for line in file.readlines():
        lines.append(line)
    text = ''.join(lines)
    file.close()
    return text

def dictToCSVfile(wordCount, path):
    newFile = open('%s' % path, 'w')
    csv_out = csv.writer(newFile)
    csv_out.writerows(wordCount)
    newFile.close()
