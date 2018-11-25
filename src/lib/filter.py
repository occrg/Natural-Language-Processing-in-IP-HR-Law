from lib.filesInOut import openTXTfile
from lib.filesInOut import loadPhrases

from lib.tokeniseTXT import splitBySentence


def onlyWordsInSentencesContaining(phrases, text):
    sentences = splitBySentence(text)
    sentencesWithPhrases = []
    for sentence in sentences:
        for phrase in phrases:
            if sentence.rfind(phrase) is not -1:
                sentencesWithPhrases.append(sentence)
                break
    filteredText = " ".join(sentencesWithPhrases)
    wordsInSentencesContainingPhrases = filteredText.split(' ')
    return wordsInSentencesContainingPhrases
