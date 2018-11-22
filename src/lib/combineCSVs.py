import sys
import os
import csv



def sortWordCount(wordCount):
    sortedWordCount = sorted(wordCount.items(), key=lambda kv: kv[1], reverse=True)
    return sortedWordCount

def combining(folderPath):
    wordCounts = {}
    for file in os.listdir(folderPath):
        currWordCount = {}
        alreadyInDict = []
        filePath = os.path.join(folderPath, file)
        currWordCount = readCSV(filePath)
        for row in currWordCount:
            if row in wordCounts.keys():
                wordCounts[row] = wordCounts[row] + currWordCount[row]
                alreadyInDict.append(row)
            else:
                wordCounts[row] = currWordCount[row]
    wordCounts = sortWordCount(wordCounts)
    return wordCounts


def readCSV(path):
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

def dictToCSVfile(wordCount, destination):
    newFile = open('%s' % destination, 'w')
    csv_out = csv.writer(newFile)
    csv_out.writerows(wordCount)
    newFile.close()


def folderToCombined(folder):
    if os.listdir(folder):
        destination = '%s/combination.csv' % folder
        if os.path.isfile(destination):
            os.remove(destination)
        wordCounts = combining(folder)
        dictToCSVfile(wordCounts, destination)
