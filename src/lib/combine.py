"""
Supplies functionality that combines dictionaries together.
"""

from lib.count import sortDict


def separateWordCountsIntoClasses(wordCounts, areasOfLaw):
    """
    Separates word counts into which class the document they represent is
    from.

    Arguments:
    wordCountsList      ([{str: (int, str)}])
            -- a list of dictionaries that are to be split based on the
               second tuple value of all its members
    areasOfLaw          ([str])
            -- a list of areas of law that are the expected values of
               the second tuple value of members of wordCounts

    Returns:
    wordCountsListList  ([[{str: (int, str)}]])
            -- a list of lists that contain dictionaries. Each list
               contains dictionaries where all its members match an
               item in areasOfLaw
    """
    wordCountsListList = []

    for a in areasOfLaw:
        wordCountsClass = []
        for wordCount in wordCounts:
            wordCountAllInClass = True
            for w in wordCount:
                if wordCount[w][1] != a:
                    wordCountAllInClass = False
                    break
            if wordCountAllInClass:
                wordCountsClass.append(wordCount)
        wordCountsListList.append(wordCountsClass)
    return wordCountsListList

def combineDicts(wordCountsList, classLabel):
    """
    Adds all the values with the same key across a list of word counts.

    Arguments:
    wordCountsList        ([{str: (int, str)}])
            -- a list of dictionaries that's common keys are to be
               combined and their respective values added
    classLabel            (str)
            -- the class label which is to be appended to the end of
               the dictionary

    Returns:
    wordCountWithClasses  ([[{str: (int, str)}]])
            -- a dictionary that contains the combined dictionaries
    """
    wordCounts = {}
    alreadyInDict = []
    for wc in wordCountsList:
        for row in wc:
            if row in wordCounts.keys():
                wordCounts[row] = wordCounts[row] + wc[row][0]
                alreadyInDict.append(row)
            else:
                wordCounts[row] = wc[row][0]
    wordCounts = sortDict(wordCounts)
    wordCountWithClasses = {}
    for w in wordCounts:
        wordCountWithClasses[w[0]] = (w[1], classLabel)
    return wordCountWithClasses
