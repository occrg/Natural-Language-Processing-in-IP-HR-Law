"""
Supplies functionality that manipulates text and splits it into a list
of words.
"""

import re
import nltk

from lib.filesio import loadPhrases


def cleanText(text):
    """
    Removes all elements of text other than plaintext words.

    Arguments:
    text  (str) -- the input text

    Returns:
    text  (str) -- the text with new lines, kerning and punctuation
                   returned
    """
    text = removeNewLines(text)
    text = substituteKerning(text)
    text = removePunctuation(text)
    return text

def combineWords(words):
    """
    Combines a list of words into a string.

    Arguments:
    words  ([str]) -- a list of words

    Returns:
    text   (str)   -- a single string of all the input words
    """
    text = ' '.join(words)
    return text

def removeNewLines(text):
    """
    Removes all characters relating to new line processing.

    Arguments:
    text  (str) -- the input text

    Returns:
    text  (str) -- the text with new line characters removed
    """
    text = text.replace('-\n', '')
    text = text.replace('\n', ' ')
    text = text.replace('\x0c', '')
    text = text.replace('—', ' ')
    return text

def substituteKerning(text):
    """
    Replaces all kerning characters with their plaintext English
    equivalents.

    Arguments:
    text  (str) -- the input text

    Returns:
    text  (str) -- the text with the kerning characters replaced
    """
    text = text.replace('ﬁ ', 'fi')
    text = text.replace('ﬁ ', 'fi')
    text = text.replace('ﬂ ', 'fl')
    text = text.replace('ﬀ ', 'ff')
    return text

def removePunctuation(text):
    """
    Removes all punctuation marks.

    Arguments:
    text  (str) -- the input textelements of text other than plaintext words.

    Returns:
    text  (str) -- the text with all punctuation marks removed
    """
    punctuation = re.compile(r'[.?!,¸/"‘“””’:;()[\]{}0-9]')
    text = punctuation.sub("", text)
    return text

def lowerCaseWords(words):
    """
    Replaces all capital letters at the start of words with lowercase
    letters.

    Arguments:
    words           ([str]) -- a list of words

    Returns:
    lowerCaseWords  ([str]) -- the same list of words with lowercase
    letters at the start of every word
    """
    lowerCaseWords = []
    for w in words:
        if w[1:].islower():
            lowerCaseWords.append(w.lower())
    return lowerCaseWords

def removeStopwords(words, stopwords):
    """
    Removes all words from ${stopwords} list.

    Arguments:
    words         ([str]) -- a list of words
    stopwords     ([str]) -- a list of words to remove from the word
                             list

    Returns:
    wordsWOstops  ([str]) -- the first list with the words from the
                             second list removed from it
    """
    wordsWOstops = []
    for w in words:
        if w not in stopwords:
            wordsWOstops.append(w)
    return wordsWOstops

def removeIntegers(words):
    """
    Removes all items from the word list that solely consist of numbers.

    Arguments:
    words  ([str]) -- a list of words

    Returns:
    words  ([str]) -- the list of words without the items which solely
                      consist of number characters.
    """
    for w in words:
        try:
            int(w)
            continue
        except ValueError:
            yield w

def lemmatise(words):
    """
    Changes variants of words in a list to a set of base words
    e.g. playing, played, plays -> play.

    Arguments:
    words            ([str]) -- a list of words

    Returns:
    lemmatisedWords  ([str]) -- the list of words with words
    """
    lemmatisedWords = []
    lemma = nltk.wordnet.WordNetLemmatizer()
    for w in words:
        l = lemma.lemmatize(w)
        lemmatisedWords.append(l)
    return lemmatisedWords


def removeEmpties(words):
    """
    Removes all empty items in the word list.

    Arguments:
    words  ([str]) -- a list of words

    Returns:
    words  ([str]) -- the list of words without empty items
    """
    while '' in words:
        words.remove('')
    return words


def splitByWord(text, stopwords):
    """
    Splits a text into a list of words, removing all stopwords.

    Arguments:
    text       (str)   -- the text that needs to be split up
    stopwords  ([str]) -- the words that are to be ignored in analysis

    Returns:
    words      ([str]) -- the list of words resulting from the text
    """
    text = cleanText(text)
    words = text.split(' ')
    words = lowerCaseWords(words)
    words = removeStopwords(words, stopwords)
    words = list(removeIntegers(words))
    words = removeEmpties(words)
    words = lemmatise(words)
    return words
