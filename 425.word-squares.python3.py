#
# [425] Word Squares
#
# https://leetcode.com/problems/word-squares/description/
#
# algorithms
# Hard (42.92%)
# Total Accepted:    16.8K
# Total Submissions: 39.1K
# Testcase Example:  '["area","lead","wall","lady","ball"]'
#
# Given a set of words (without duplicates), find all word squares you can
# build from them.
#
# A sequence of words forms a valid word square if the kth row and column read
# the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"] forms a word
# square because each word reads the same both horizontally and vertically.
#
#
# b a l l
# a r e a
# l e a d
# l a d y
#
#
# Note:
#
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
#
#
#
# Example 1:
#
# Input:
# ["area","lead","wall","lady","ball"]
#
# Output:
# [
# ⁠ [ "wall",
# ⁠   "area",
# ⁠   "lead",
# ⁠   "lady"
# ⁠ ],
# ⁠ [ "ball",
# ⁠   "area",
# ⁠   "lead",
# ⁠   "lady"
# ⁠ ]
# ]
# "wallx"
# "areay
# "lebcd
# "lacke
# "xydep
#
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
#
#
#
# Example 2:
#
# Input:
# ["abat","baba","atan","atal"]
#
# Output:
# [
# ⁠ [ "baba",
# ⁠   "abat",
# ⁠   "baba",
# ⁠   "atan"
# ⁠ ],
# ⁠ [ "baba",
# ⁠   "abat",
# ⁠   "baba",
# ⁠   "atal"
# ⁠ ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
#


class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        res, self.dic = [], dict()
        words = list(set(words))
        for word in words:
            for i in range(len(word)+1):
                if word[:i] not in self.dic:
                    self.dic[word[:i]] = []
                self.dic[word[:i]].append(word)
        self.DFS(words, [], res, len(words[0]), "")
        return res

    def DFS(self, words, cur, res, n, prefix):
        if prefix not in self.dic:
            return
        for word in self.dic[prefix]:
            nxt, nc = "", cur+[word]
            if len(nc) == n:
                res.append(nc)
                continue
            for j in range(len(nc)):
                nxt += nc[j][len(nc)]
            self.DFS(words, nc, res, n, nxt)
