import re
import nltk

from lib.filesInOut import loadPhrases
from lib.filesInOut import openTXTfile

def cleanText(text):
    text = removeNewLines(text)
    text = substituteKerning(text)
    text = removePunctuation(text)
    return text

def combineWords(words):
    block = ' '.join(words)
    return block

def removeNewLines(text):
    wordsOnTwoLines = text.replace('-\n', '')
    noNewLines = wordsOnTwoLines.replace('\n', ' ')
    noX0Cs = noNewLines.replace('\x0c', '')
    return noX0Cs

def substituteKerning(text):
    replaceFis = text.replace('ﬁ ', 'fi')
    replaceFls = replaceFis.replace('ﬂ ', 'fl')
    replaceFfs = replaceFls.replace('ﬀ ', 'ff')
    return replaceFis

def removePunctuation(text):
    punctuation = re.compile(r'[.?!,/"“””’:;()[\]{}0-9]')
    textWOPuncts = punctuation.sub("", text)
    return textWOPuncts

def lowerCaseWords(words):
    lowerCaseWords = []
    for w in words:
        if w[1:].islower():
            lowerCaseWords.append(w.lower())
    return lowerCaseWords

def removeStopwords(words):
    stopwords = loadPhrases('lists/stopwords.txt')
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

def lemmatise(words):
    lemmatisedWords = []
    lemma = nltk.wordnet.WordNetLemmatizer()
    for w in words:
        l = lemma.lemmatize(w)
        lemmatisedWords.append(l)
    return lemmatisedWords

def lemmatisePhrases(phrases):
    lemmatisedPhrases = []
    for p in phrases:
        phraseInWords = p.split()
        lemmatisedPhraseInWords = lemmatise(phraseInWords)
        lemmatisedPhrase = ' '.join(lemmatisedPhraseInWords)
        lemmatisedPhrases.append(lemmatisedPhrase)
    return lemmatisedPhrases


def removeEmpties(words):
    while '' in words:
        words.remove('')
    return words

def separatingIntoSentenceBlocks(text):
    pars = text.split("\n\n")
    parsSplitBySentence = []
    for p in pars:
        if isinstance(p, str):
            pNoNewLines = removeNewLines(p)
            parsSplitBySentence.append(pNoNewLines.split(". "))
            sentencesWempties = [sentence for sublist in parsSplitBySentence for sentence in sublist]
            sentences = [x for x in sentencesWempties if x]
    return sentences

def cleanSentencesAsWords(sentences):
    splitSentences = []
    for s in sentences:
        s = splitByWord(s)
        splitSentences.append(s)
    return splitSentences

def joinWordsInList(listOfLists):
    joinedBlocks = []
    for l in listOfLists:
        block = ' '.join(l)
        joinedBlocks.append(block)
    return joinedBlocks

def splitByWord(text):
    text = cleanText(text)
    words = text.split(' ')
    words = lowerCaseWords(words)
    words = removeStopwords(words)
    words = list(removeIntegers(words))
    words = removeEmpties(words)
    words = lemmatise(words)
    return words

def splitBySentence(text):
    sentenceBlocks = separatingIntoSentenceBlocks(text)
    sentencesSplitByWords = cleanSentencesAsWords(sentenceBlocks)
    sentencesWempties = joinWordsInList(sentencesSplitByWords)
    sentences = removeEmpties(sentencesWempties)
    return sentences

def TXTtoWordList(origin):
    text = openTXTfile(origin)
    words = splitByWord(text)
    return words

def folderOfTXTsToWordLists(originFolder):
    wordLists = []
    for file in os.listdir(originFolder):
        filePath = os.path.join(originFolder, file)
        wordList = TXTtoWordList(filePath)
        wordLists.append(wordList)
        return wordLists
