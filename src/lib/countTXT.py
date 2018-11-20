import os
import csv

from lib.tokeniseTXT import tokeniseText


def sortWordCount(wordCount):
    sortedWordCount = sorted(wordCount.items(), key=lambda kv: kv[1], reverse=True)
    return sortedWordCount

def countWords(words):
    wordCount = {}
    for w in words:
        if w in wordCount:
            wordCount[w] += 1
        else:
            wordCount[w] = 1
    sortedWordCount = sortWordCount(wordCount)
    return sortedWordCount


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


def TXTtoCSVwordCount(origin, destination):
    text = openTXTfile(origin)
    words = tokeniseText(text)
    wordCount = countWords(words)
    dictToCSVfile(wordCount, destination)

def folderOfTXTsToCSVs(originFolder, destinationFolder):
    for file in os.listdir(originFolder):
        filePath = os.path.join(originFolder, file)
        filename, ext = file.split(".")
        destination = "%s/%s.csv" % (destinationFolder, filename)
        TXTtoCSVwordCount(filePath, destination)
