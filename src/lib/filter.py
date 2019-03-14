"""
Supplies functionality to filter out items of text that do not meet
certain requirements.
"""

from lib.tokenise import cleanSentence


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
