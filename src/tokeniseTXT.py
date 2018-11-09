import sys

import string
import csv

def removeNewLines(text):
    return text.replace('\n', ' ')

def removePunctuation(text):
    remove_punct_map = dict.fromkeys(map(ord, string.punctuation))
    return text.translate(remove_punct_map)

def lowerCaseWords(words):
    lowerCaseWords = []
    for w in words:
        if w[1:].islower():
            lowerCaseWords.append(w.lower())
    return lowerCaseWords

def loadStopwords():
    file = open('stopwords.txt', 'r')
    stopwords = []
    for line in file.readlines():
        newline = line.replace('\n', '')
        stopwords.append(newline)
    file.close()
    return stopwords

def removeStopwords(words):
    stopwords = loadStopwords()
    wordsWOStops = []
    for w in words:
        if w not in stopwords:
            wordsWOStops.append(w)
    return wordsWOStops

def removeIntegers(words):
    for w in words:
        try:
            int(w)
            continue
        except ValueError:
            yield w

def removeEmpties(words):
    while '' in words:
        words.remove('')
    return words

def tokeniseText(text):
    text = removeNewLines(text)
    text = removePunctuation(text)
    words = text.split(' ')
    words = lowerCaseWords(words)
    words = removeStopwords(words)
    words = list(removeIntegers(words))
    words = removeEmpties(words)
    return words


def sortWordCount(wordCount):
    sortedWordCount = sorted(wordCount.items(), key=lambda kv: kv[1])
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
    return text
    file.close()


def dictToCSVfile(wordCount, path):
    filename, format = path.split(".")
    newFile = open('%s.csv' % filename, 'w')
    csv_out = csv.writer(newFile)
    csv_out.writerows(wordCount)
    newFile.close()


def main():
    file = sys.argv[1]
    origin = 'TXTs/%s' % file
    destination = 'wordCounts/%s' % file
    text = openTXTfile(origin)
    words = tokeniseText(text)
    wordCount = countWords(words)
    dictToCSVfile(wordCount, destination)

if __name__ == '__main__':
    main()
