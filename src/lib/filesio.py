"""
Supplies functionality to input and output files.
"""

import os


def stringToTXTfile(text, path):
    """
    Stores string as a .txt file at ${path}.

    Arguments:
    text  (str) -- the text that needs to be stored
    path  (str) -- the path where the text should be stored
    """
    newFile = open('%s' % path, 'w')
    newFile.write('%s' % text + '\n')
    newFile.close()

def txtFileToString(path):
    """
    Loads the .txt file at ${path} as a string.

    Arguments:
    path  (str) -- the path where the desired .txt file is

    Returns:
    text  (str) -- the text that was stored in the .txt file
    """
    file = open('%s' % path, 'r')
    lines = []
    for line in file.readlines():
        lines.append(line)
    text = ''.join(lines)
    file.close()
    return text


def dictToCSVfile(wordCount, path):
    """
    Stores string as a .txt file at ${path}.

    Arguments:
    wordCount  ({str: (int, str)})
            -- the dictionary that needs to be stored with the keys
               stored as the first column, the first value of the tuple
               stored as the second column and the second value of the
               tuple stored as the third column
    path       (str)
            -- the path where the dictionary should be stored
    """
    table = []
    table.append("word/phrase,value,class")
    for w in wordCount:
        table.append("%s,%s,%s" % (w, wordCount[w][0], wordCount[w][1]))
    newFile = open('%s' % path, 'w')
    newFile.write("\n".join(table))
    newFile.close()

def csvFileToDict(path):
    """
    Loads the .csv file at ${path} as a dictionary.

    Arguments:
    path       (str)
            -- the path where the desired .csv file is

    Returns:
    wordCount  ({str: (int, str)}})
            -- a dictionary containing the first column of the csv file
               as the keys and a tuple consisting of the second and
               third columns of the csv file
    """
    file = open('%s' % path, 'r')
    wordCount = {}
    for line in file.readlines()[1:]:
        newLine = line.replace('\n', '')
        w, c0, c1 = newLine.split(',')
        wordCount[w] = (int(c0), c1)
    file.close()
    return wordCount


def loadPhrases(path):
    """
    Loads a list of phrases or words at ${path} as a list of strings.

    Arguments:
    path     (str)   -- the path where the desired .txt file is

    Returns:
    phrases  ([str]) -- the list of words/phrases that were stored in
                        the .txt file
    """
    file = open('%s' % path, 'r')
    phrases = []
    for line in file.readlines():
        newline = line.replace('\n', '')
        phrases.append(newline)
    file.close()
    return phrases
