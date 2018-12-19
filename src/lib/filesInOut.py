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

def readCSVinDict(path):
    if(not os.path.isfile(path)):
        raise ValueError("File does not exist. File path (%s) wrong." % path)
    file = open('%s' % path, 'r')
    wordCount = {}
    for line in file.readlines():
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

def textVarToTXTfile(text, destination):
    newFile = open('%s' % destination, 'w')
    newFile.write('%s' % text + '\n')
    newFile.close()
