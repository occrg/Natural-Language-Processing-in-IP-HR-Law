"""
Supplies functionality that manipulates text and splits it into a list
of words.
"""

import re
import nltk


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
    text = text.replace('(cid:222)', 'fi')
    text = text.replace('(cid:223)', 'fl')
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
    punctuation = re.compile(r'[.?…!,¸_/"º`\'‘“””’%:;()[\]<>{}0-9]')
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
    Removes all words from ${words} that are in ${stopwords}.

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

def removeStopstrings(words, stopstrings):
    """
    Removes all words that contain any elements of ${stopstrings} from
    ${words}.
    Arguments:
    words           ([str])
            -- a list of words
    stopstrings     ([str])
            -- a list of strings that indicate a word should be removed
               if the string is contained in that word

    Returns:
    wordsWOstops    ([str])
            -- the first list with the appropriate words removed
    """
    wordsWOstops = []
    for w in words:
        stopInW = False
        for string in stopstrings:
            if string in w:
                stopInW = True
        if not stopInW:
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

def separatingIntoSentenceBlocks(text):
    """
    Splits ${text} into sentences.

    Arguments:
    text       (str)   -- a string representing the text that is to be
                          split into sentences

    Returns:
    sentences  ([str]) -- a list of strings, each representing a
                          sentence from ${text}
    """
    pars = text.split("\n\n")
    parsSplitBySentence = []
    for p in pars:
        if isinstance(p, str):
            pNoNewLines = removeNewLines(p)
            parsSplitBySentence.append(pNoNewLines.split(". "))
            sentencesWempties = [sentence for sublist in parsSplitBySentence for sentence in sublist]
            sentences = [x for x in sentencesWempties if x]
    return sentences

def cleanSentence(sentence):
    """
    Strips ${sentence} to only include lowercase plaintext words.

    Arguments:
    sentence  (str) -- a string representing the sentence that is to be
                       cleaned
    """
    cleanedSentence = []
    sentence = cleanText(sentence)
    words = sentence.split(' ')
    words = lowerCaseWords(words)
    words = list(removeIntegers(words))
    words = removeEmpties(words)
    cleanedSentence = ' '.join(words)
    return cleanedSentence

def joinWordsInList(listOfLists):
    """
    Converts a list of lists of strings into a list of strings where
    each item of the inner list is separated by a space.

    Arguments:
    listOfLists   ([[str]])
            -- a list of lists where the outer list represents the
               whole text, the inner lists each represent a sentence
               and each of the items in the inner list represent a word
               in the corresponding sentence

    Returns:
    joinedBlocks  ([str])
            -- a list of strings where each string consists of all the
               items of an inner list of ${listOfLists} separated by a
               space
    """
    joinedBlocks = []
    for l in listOfLists:
        block = ' '.join(l)
        joinedBlocks.append(block)
    return joinedBlocks


def splitByWord(text, stopwords, stopstrings):
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
    words = removeStopstrings(words, stopstrings)
    words = list(removeIntegers(words))
    words = removeEmpties(words)
    words = lemmatise(words)
    return words

def splitBySentence(text):
    """
    Determines how ${text} is split into sentences.

    Arguments:
    text       (str)   -- a string representing the text that is to be
                          split into sentences

    Returns:
    sentences  ([str]) -- a list of strings, each representing a
                          sentence from ${text}
    """
    sentenceBlocks = separatingIntoSentenceBlocks(text)
    # sentencesSplitByWords = cleanSentencesAsWords(sentenceBlocks)
    # sentencesWempties = joinWordsInList(sentencesSplitByWords)
    sentences = removeEmpties(sentenceBlocks)
    return sentences

def removeSentencesWithoutPhrases(phrases, sentences):
    """
    Removes each sentence from ${sentences} which does not include any
    phrase from ${phrases}.

    Arguments:
    phrases               ([str])
            -- a list of strings with each string representing a phrase
    sentences             ([str])
            -- a list of strings with each string with each string
               representing a sentence
    Returns:
    sentencesWithPhrases  ([str])
            -- the ${sentences} list with all sentences that do not
               contain a phrase from ${phrases} removed
    """
    sentencesWithPhrases = []
    for sentence in sentences:
        cleanedSentence = cleanSentence(sentence)
        for phrase in phrases:
            if cleanedSentence.rfind(phrase) is not -1:
                sentencesWithPhrases.append(sentence)
                break
    return sentencesWithPhrases
