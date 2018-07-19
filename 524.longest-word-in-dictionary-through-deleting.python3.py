#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (43.38%)
# Total Accepted:    25.2K
# Total Submissions: 58.1K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
#
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
#
# Example 1:
#
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
#
#
#
#
# Example 2:
#
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
#
#
#
# Note:
#
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
#


class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d = sorted(d, key=lambda x: (-len(x), x))
        for i in range(len(d)):
            if self.check(d[i], s):
                return d[i]
        return ""

    def check(self, a, b):
        if len(a) > len(b):
            return False
        if len(a) == len(b):
            return a == b
        L, R = 0, 0
        while L < len(a) and R < len(b):
            if a[L] == b[R]:
                L, R = L+1, R+1
            else:
                R += 1
        if L == len(a):
            return True
        return False
