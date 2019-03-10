import math


def totalWords(wordCount):
    """
    Counts the number of words in a document.

    Arguments:
    wordCount  ({str: int})
            --

    Returns:
    sum        (int)
            --
    """
    sum = 0
    for w in wordCount:
        sum += wordCount[w]
    return sum

def termFrequency(wordCounts):
    """
    Finds the term frequency of each term in each document. This is
    how often each word appears as a proportion of all the terms in
    each document.

    Arguments:
    wordCounts    ([{str: int}])
            -- a list of dictionaries with each dictionary representing
               a different document's term count

    Returns:
    tfWordCounts  ([{str: int}])
            -- the same list of dictionaries but with all values
               divided by the total number of terms in that document
    """
    tfWordCounts = []
    for wordCount in wordCounts:
        sum = totalWords(wordCount)
        tfWordCount = {}
        for w in wordCount:
            tfWordCount[w] = wordCount[w] / sum
        tfWordCounts.append(tfWordCount)
    return tfWordCounts

def inverseDocumentFrequency(wordCounts):
    """
    Finds the inverse document frequency of each term in each document.
    This is how many documents the term appears in as a proportion of
    how many documents there are in total.

    Arguments:
    wordCounts    ([{str: int}])
            -- a list of dictionaries with each dictionary representing
               a different document's term count

    Returns:
    tfWordCounts  ([{str: int}])
            -- the same list of dictionaries but with all values
               divided by the total number of words in that document
    """
    idfWordCounts = []
    N = len(wordCounts)
    for wordCount in wordCounts:
        idfWordCount = {}
        for w in wordCount:
            nt = 0
            for wordCountCmp in wordCounts:
                if w in wordCountCmp:
                    nt += 1
            r = math.log(N / nt, 10)
            idfWordCount[w] = r
        idfWordCounts.append(idfWordCount)
    return idfWordCounts

def tfidf(wordCounts):
    """
    Finds the term frequency-inverse document frequency of each term in
    each document. This is the term frequency of each term multiplied
    by the inverse document frequency of each term (as specified above).

    Arguments:
    wordCounts    ([{str: int}])
            -- a list of dictionaries with each dictionary representing
               a different document's term count

    Returns:
    tfWordCounts  ([{str: int}])
            -- the same list of dictionaries but with all values
               converted to term frequency-inverse document frequency
    """
    tfidfWordCounts = []
    tfWordCounts = termFrequency(wordCounts)
    idfWordCounts = inverseDocumentFrequency(wordCounts)
    for i in range(len(tfWordCounts)):
        wordCount = {}
        for w in tfWordCounts[i]:
            v = tfWordCounts[i][w] * idfWordCounts[i][w]
            wordCount[w] = v
        tfidfWordCounts.append(wordCount)
    return tfidfWordCounts
