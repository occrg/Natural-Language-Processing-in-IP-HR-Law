"""
Supplies functionality to input and output files.
"""

import os
import numpy as np
import datetime


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


def countToCSVfile(wordCount, path):
    """
    Stores an object of the same form as ${wordCount} as a .csv file at
    ${path}.

    Arguments:
    wordCount  ({str: int})
            -- the dictionary that needs to be stored with the key
               stored as the first column and the value as the second
               column
    path       (str)
            -- the path where the dictionary is to be stored
    """
    table = []
    table.append("word/phrase,value,class")
    for w in wordCount:
        table.append("%s,%s" % (w, wordCount[w]))
    newFile = open('%s' % path, 'w')
    newFile.write("\n".join(table))
    newFile.close()

def csvFileToCount(path):
    """
    Loads the .csv file at ${path} as a dictionary in the form of
    ${wordCount}.

    Arguments:
    path       (str)
            -- the path where the desired .csv file is

    Returns:
    wordCount  ({str: (int, str)}})
            -- a dictionary with the first column of the csv file as
               the its keys and the second column of the csv file as
               the its values
    """
    file = open('%s' % path, 'r')
    wordCount = {}
    for line in file.readlines()[1:]:
        newLine = line.replace('\n', '')
        w, n = newLine.split(',')
        wordCount[w] = float(n)
    file.close()
    return wordCount


def documentDetailsToCSVfile(documentDetails, path):
    """
    Stores an object of the same form as ${documentDetails} as a .csv
    file at ${path}.

    Arguments:
    documentDetails  ([{str: str, str: str, str: str, str: str,
                        str: str, str: datetime, str: int, str: int,
                        str: float, str: float, str: float,
                        str: float}])
            -- a list of dictionaries where each dictionary in the list
               is to be represented by a row in the csv file and each
               key is represented by a column in the csv file

    path             str
            -- the path where the dictionary is to be stored
    """
    table = []
    table.append(                                                            \
    "title,journal,pdf path,txt path,count path,frequency path,date,class,training,hr prob,ip prob,user prob,creator prob")
    for document in documentDetails:
        table.append("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (
            document['title'], document['journal'], document['pdfPath'],     \
            document['txtPath'], document['countPath'],                      \
            document['frequencyPath'], document['date'], document['class'],  \
            document['test'], document['hrProb'], document['ipProb'],        \
            document['userProb'], document['creatorProb']))
    newFile = open('%s' % path, 'w')
    newFile.write("\n".join(table))
    newFile.close()

def csvFileToDocumentDetails(path):
    """
    Loads the .csv file at ${path} as a dictionary in the form of
    ${documentDetails}.

    Arguments:
    path             str
            -- the path where the dictionary is to be stored

    Returns:
    documentDetails  ([{str: str, str: str, str: str, str: str,
                        str: str, str: datetime, str: int, str: int,
                        str: float, str: float, str: float,
                        str: float}])
            -- a list of dictionaries where each dictionary has been
               retrieved from a row of the csv file at ${path} and each
               key has been retrieved from a column of that csv file
    """
    file = open('%s' % path, 'r')
    documentDetails = []
    for line in file.readlines()[1:]:
        newLine = line.replace('\n', '')
        title, journal, pdfPath, txtPath, countPath, frequencyPath,          \
            stringDate, classLabel, training, hrProb, ipProb, userProb,      \
            creatorProb = newLine.split(',')
        details = {'title':title, 'journal':journal, 'pdfPath':pdfPath,      \
            'txtPath':txtPath, 'countPath':countPath,                        \
            'frequencyPath':frequencyPath,                                   \
            'date': datetime.datetime.strptime(stringDate, '%Y-%m-%d').date()\
            ,'class':int(classLabel), 'test':int(training),                  \
            'hrProb':float(hrProb), 'ipProb':float(ipProb),                  \
            'userProb':float(userProb),'creatorProb':float(creatorProb)}
        documentDetails.append(details)
    file.close()
    return documentDetails


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
