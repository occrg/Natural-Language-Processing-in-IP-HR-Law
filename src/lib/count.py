"""
Supplies functionality to count the occurence of words in a string.
"""

from lib.tokenise import splitByWord


def countWords(words, classLabel):
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
            -- a list of keys representing unique words with
               corresponding values representing the number of
               occurences the words have
    """
    wordCount = {}
    for w in words:
        if (w, classLabel) in wordCount:
            wordCount[(w, classLabel)] += 1
        else:
            wordCount[(w, classLabel)] = 1
    return wordCount


def stringToWordCount(text, classLabel, stopwords, stopstrings):
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
    wordCountWithClasses  ({(str, str): int})
                -- a list of keys which are tuples with its first value
                   being a word and the second value being the class of
                   the document that word was found in. The value is
                   the number of times that word appeared in a document
    """
    words = splitByWord(text, stopwords, stopstrings)
    wordCount = countWords(words, classLabel)
    return wordCount
