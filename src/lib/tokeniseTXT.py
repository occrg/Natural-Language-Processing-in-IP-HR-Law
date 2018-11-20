import re
import nltk


def splitByParagraph(text):
    return text.split("\n\n")

def splitBySentence(text):
    pars = splitByParagraph(text)
    for p in pars:
        pNoNewLines = p.replace('\n', ' ')
        sentencesInPars.append(pNoNewLines.split(". "))
        sentences = [sentence for par in sentencesInPars for sentence in par]
    return setences

def combineWords(words):
    block = ' '.join(words)
    return block

def removeNewLines(text):
    wordsOnTwoLines = text.replace('-\n', '')
    noNewLines = wordsOnTwoLines.replace('\n', ' ')
    return noNewLines

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

def loadStopwords():
    stopwordsFileLocation = 'lists/stopwords.txt'
    file = open('%s' % stopwordsFileLocation, 'r')
    stopwords = []
    for line in file.readlines():
        newline = line.replace('\n', '')
        stopwords.append(newline)
    file.close()
    return stopwords

def splitByWord(text):
    return text.split(' ')

def removeStopwords(words):
    stopwords = loadStopwords()
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
    nltk.download('wordnet')
    lemma = nltk.wordnet.WordNetLemmatizer()
    for w in words:
        l = lemma.lemmatize(w)
        lemmatisedWords.append(l)
    return lemmatisedWords

def removeEmpties(words):
    while '' in words:
        words.remove('')
    return words

def tokeniseText(text):
    text = removeNewLines(text)
    text = substituteKerning(text)
    text = removePunctuation(text)
    words = splitByWord(text)
    words = lowerCaseWords(words)
    words = removeStopwords(words)
    words = list(removeIntegers(words))
    words = removeEmpties(words)
    words = lemmatise(words)
    return words
