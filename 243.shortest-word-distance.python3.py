#
# [243] Shortest Word Distance
#
# https://leetcode.com/problems/shortest-word-distance/description/
#
# algorithms
# Easy (53.99%)
# Total Accepted:    46K
# Total Submissions: 85.2K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"
# coding"\n"practice"'
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
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
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
#


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pre, pre_pos, res = None, -1, len(words)
        for i in range(len(words)):
            if words[i] == word1:
                if pre == word2:
                    res = min(res, i-pre_pos)
                pre, pre_pos = words[i], i
            elif words[i] == word2:
                if pre == word1:
                    res = min(res, i-pre_pos)
                pre, pre_pos = words[i], i
        return res
