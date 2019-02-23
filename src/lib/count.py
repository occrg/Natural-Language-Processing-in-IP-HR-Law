"""
Supplies functionality to count the occurence of words in a string.
"""

from lib.tokenise import splitByWord


def sortDict(dict):
    """
    Sorts a dictionary in descending order of its values.

    Arguments:
    dict        ({str: int}})
                -- a list of keys representing unique words with
                   corresponding values representing the number of
                   occurences the words have

    Returns:
    sortedDict  ({str: int}})
                -- the same words placed in descending order of their
                   values
    """
    sortedDict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    return sortedDict

def countWords(words):
    """
    Counts the number of times each unique word appears in a list of
    words.

    Arguments:
    words            ([str])
            -- a list of words that appear in a document (includes
               repeated words)

    Returns:
    sortedWordCount  ({str: int}})
            -- a list of keys representing unique words with
               corresponding values representing the number of
               occurences the words have
    """
    wordCount = {}
    for w in words:
        if w in wordCount:
            wordCount[w] += 1
        else:
            wordCount[w] = 1
    sortedWordCount = sortDict(wordCount)
    return sortedWordCount


def stringToWordCount(text, classLabel, stopwords):
    """
    Converts text to a list of words and counts the occurrences then
    appends the class label of the document that the word originated
    from.

    Arguments:
    text                  (str)
                -- the text from a document
    classLabel            (str)
                -- the classification of the document
    stopwords             ([str])
                -- the words that are to be ignored in analysis


    Returns:
    wordCountWithClasses  ({str: (int, str)})
                -- a list of keys representing unique words with
                   corresponding values which are tuples with the first
                   element representing the number of occurrences the
                   words have and the second representing the class
                   label of the document which the word originated from
    """
    words = splitByWord(text, stopwords)
    wordCount = countWords(words)
    wordCountWithClasses = {}
    for w in wordCount:
        wordCountWithClasses[w[0]] = (w[1], classLabel)
    return wordCountWithClasses
