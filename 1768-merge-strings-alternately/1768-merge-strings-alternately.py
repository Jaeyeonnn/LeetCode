class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""

        word1_len = len(word1)
        word2_len = len(word2)
        greatest_len = max([word1_len, word2_len])
        counter = 0

        while counter != greatest_len:
            if counter < word1_len:
                merged += word1[counter]
            if counter < word2_len:
                merged += word2[counter]
            counter += 1

        return merged