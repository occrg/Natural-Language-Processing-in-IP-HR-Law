import math


"""

"""
class FrequencyCalc:


    def tfidf(self, tf, idf):
        """

        """
        tfidf = []
        for i in range(len(tf)):
            v = tf[i] * idf[i]
            tfidf.append(v)
        return tfidf


    def tf(self, wordCount):
        """

        """
        tf = []
        sum = self.__totalWords(wordCount)
        for (w, n) in wordCount:
            tf.append(int(n) / sum)
        return tf

    def idf(self, wordCount, wordLists):
        """

        """
        idf = []
        N = len(wordLists)
        for (w, n) in wordCount:
            nt = 0
            for words in wordLists:
                if w in words:
                    nt += 1
            r = math.log(N / nt, 10)
            idf.append(r)
        return idf


    def __totalWords(self, wordCount):
        """

        """
        sum = 0
        for (w, n) in wordCount:
            sum += int(n)
        return sum
