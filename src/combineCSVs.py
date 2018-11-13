import sys
import os

import csv


def readCSV(path):
    file = open('%s' % path, 'r')
    wordCount = {}
    for line in file.readlines():
        index, rhs = line.split(",")
        value = int(rhs)
        wordCount[index] = value
    file.close()
    return wordCount

def dictToCSVfile(wordCount, path):
    newFile = open('%s' % path, 'w')
    csv_out = csv.writer(newFile)
    csv_out.writerows(wordCount)
    newFile.close()

def sortWordCount(wordCount):
    sortedWordCount = sorted(wordCount.items(), key=lambda kv: kv[1])
    return sortedWordCount


def combineCSVs(origin):
    wordCounts = {}
    for file in os.listdir(origin):
        currWordCount = {}
        alreadyInDict = []
        filePath = os.path.join(origin, file)
        currWordCount = readCSV(filePath)
        for row in currWordCount:
            if row in wordCounts.keys():
                wordCounts[row] = wordCounts[row] + currWordCount[row]
                alreadyInDict.append(row)
            else:
                wordCounts[row] = currWordCount[row]
    wordCounts = sortWordCount(wordCounts)
    return wordCounts


def main():
    if(len(sys.argv) != 3):
        raise ValueError("Wrong number of arguments. There should be 2 (excluding Python file name).")
    origin = sys.argv[1]
    destination = sys.argv[2]
    wordCounts = combineCSVs(origin)
    dictToCSVfile(wordCounts, destination)

if __name__ == '__main__':
    main()
