#
# [245] Shortest Word Distance III
#
# https://leetcode.com/problems/shortest-word-distance-iii/description/
#
# algorithms
# Medium (51.58%)
# Total Accepted:    28.8K
# Total Submissions: 55.8K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n
# "makes"\n"coding"'
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in
# the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#
# Input: word1 = “makes”, word2 = “coding”
# Output: 1
#
#
#
# Input: word1 = "makes", word2 = "makes"
# Output: 3
#
#
# Note:
# You may assume word1 and word2 are both in the list.
#


class Solution:
    def shortestWordDistance(self, words, word1, word2):
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
