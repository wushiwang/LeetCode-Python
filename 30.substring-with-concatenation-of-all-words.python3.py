#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (22.29%)
# Total Accepted:    98.8K
# Total Submissions: 443K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
#
# Example 1:
#
#
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input:
# ⁠ s = "wordgoodstudentgoodword",
# ⁠ words = ["word","student"]
# Output: []
#


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Check words' length
        if len(words) == 0:
            return list()
        if len(words) > 1:
            for i in range(1, len(words)):
                if len(words[i]) != len(words[i-1]):
                    return list()
        dic, res, m = {}, list(), len(words[0])
        for w in words:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] = dic[w] + 1
        length = m * len(words)

        for i in range(0, m):
            L, R = i, i
            while R <= len(s) - m:
                if R - L == length:
                    res.append(L)
                    if s[L:L+m] in dic:
                        dic[s[L:L+m]] = dic[s[L:L+m]]+1
                    L = L + m
                w = s[R:R+m]
                if w in dic:
                    if dic[w] != 0:
                        dic[w] = dic[w] - 1
                        R = R + m
                    else:
                        while dic[w] == 0:
                            nw = s[L:L+m]
                            if nw in dic:
                                dic[nw] = dic[nw] + 1
                            L = L + m
                else:
                    R = R + m
                    self.back(L, R, s, dic, m)
                    L = R
            if R - L == length:
                res.append(L)
            self.back(L, R, s, dic, m)
            L = R
        return res

    def back(self, L, R, s, dic, m):
        while L != R:
            w = s[L:L+m]
            if w in dic:
                dic[w] = dic[w] + 1
            L = L + m
