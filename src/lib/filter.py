from lib.filesInOut import openTXTfile
from lib.filesInOut import loadPhrases

from lib.tokeniseTXT import splitBySentence


def excludeGivenPhrases(phraseWords, words):
    excludingPhrases = []
    for w in words:
        if w not in phraseWords:
                excludingPhrases.append(w)
    return excludingPhrases

def collateAllWordsInPhrases(phrases):
    phraseWords = []
    for p in phrases:
        phraseSplitIntoWords = p.split()
        for psplit in phraseSplitIntoWords:
            phraseWords.append(psplit)
    return phraseWords

def removeSentencesWithoutPhrases(phrases, sentences):
    sentencesWithPhrases = []
    for sentence in sentences:
        for phrase in phrases:
            if sentence.rfind(phrase) is not -1:
                sentencesWithPhrases.append(sentence)
                break
    return sentencesWithPhrases

def onlyWordsInSentencesContaining(phrases, text):
    sentences = splitBySentence(text)
    sentencesFiltered = removeSentencesWithoutPhrases(phrases, sentences)
    joinedSentencesFiltered = " ".join(sentencesFiltered)
    phraseWords = collateAllWordsInPhrases(phrases)
    wordsInSentencesContainingPhrases = joinedSentencesFiltered.split(' ')
    sentencesWithoutPhraseWords = excludeGivenPhrases(phraseWords, wordsInSentencesContainingPhrases)
    return sentencesWithoutPhraseWords
