#
# [472] Concatenated Words
#
# https://leetcode.com/problems/concatenated-words/description/
#
# algorithms
# Hard (31.52%)
# Total Accepted:    13K
# Total Submissions: 41.1K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# Given a list of words (without duplicates), please write a program that
# returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words in the given array.
#
# Example:
#
# Input:
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat"
# can be concatenated by "rat", "cat", "dog" and "cat".
#
#
#
# Note:
#
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.
#


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        self.dic = set()
        for word in words:
            self.dic.add(word)
        res = []
        for word in words:
            if self.check(word, 0):
                res.append(word)
        return res

    def check(self, word, cnt):
        if len(word) == 0:
            return cnt >= 2
        for i in range(len(word)):
            if word[:i+1] in self.dic:
                if self.check(word[i+1:], cnt+1):
                    return True
        return False
