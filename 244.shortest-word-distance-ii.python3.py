#
# [244] Shortest Word Distance II
#
# https://leetcode.com/problems/shortest-word-distance-ii/description/
#
# algorithms
# Medium (41.89%)
# Total Accepted:    32.4K
# Total Submissions: 77.4K
# Testcase Example:  '["WordDistance","shortest","shortest"]\n[[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]'
#
# Design a class which receives a list of words in the constructor, and
# implements a method that takes two words word1 and word2 and return the
# shortest distance between these two words in the list. Your method will be
# called repeatedly many times with different parameters. 
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
#
#
#
# Input: word1 = "makes", word2 = "coding"
# Output: 1
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
#
import math


class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.pos = dict()
        self.dic = dict()
        for i in range(len(words)):
            if words[i] in self.pos:
                self.pos[words[i]].append(i)
            else:
                self.pos[words[i]] = [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1, word2) in self.dic:
            return self.dic[(word1, word2)]
        L, R, res = 0, 0, math.inf
        p1, p2 = self.pos[word1], self.pos[word2]
        while L < len(p1) and R < len(p2):
            a, b = p1[L], p2[R]
            if a < b:
                res = min(res, b-a)
                L += 1
            else:
                res = min(res, a-b)
                R += 1
        self.dic[(word1, word2)] = res
        self.dic[(word2, word1)] = res
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
