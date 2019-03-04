"""
Supplies functionality to count the occurence of words in a string.
"""

from lib.tokenise import splitByWord


def countWords(words):
    """
    Counts the number of times each unique word appears in a list of
    words.

    Arguments:
    words      ([str])
            -- a list of words that appear in a document (includes
               repeated words)
    classLabel            (str)
            -- the classification of the document the word originates from

    Returns:
    wordCount  ({str: int}})
            -- a dictionary with keys representing unique words in a document
               with corresponding values representing the count of the
               word in that document
    """
    wordCount = {}
    for w in words:
        if w in wordCount:
            wordCount[w] += 1
        else:
            wordCount[w] = 1
    return wordCount


def stringToWordCount(text, stopwords, stopstrings):
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
    stopstrings           ([str])
            -- a list of strings, that if included in a word,
               should disqualify a word for being considered in
               analysis


    Returns:
    wordCount  ({str: int}})
            -- a dictionary with keys representing unique words in a document
               with corresponding values representing the count of the
               word in that document
    """
    words = splitByWord(text, stopwords, stopstrings)
    wordCount = countWords(words)
    return wordCount
