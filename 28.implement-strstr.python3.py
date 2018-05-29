#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (29.18%)
# Total Accepted:    277K
# Total Submissions: 948.8K
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.KMP(haystack, needle)

    def KMP(self, s, p):
        def __getLPS(p):
            '''
            Get LPS array for pattern p
            '''
            lps, i, j = [-1 for x in range(len(p)+1)], 0, -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i, j = i + 1, j + 1
                    lps[i] = j
                else:
                    j = lps[j]
            return lps
        lps = __getLPS(p)
        i, j = 0, 0
        while i < len(s):
            if j == len(p):
                return i - len(p)
            elif j == -1 or s[i] == p[j]:
                i, j = i + 1, j + 1
            else:
                j = lps[j]
        if j == len(p):
            return i - len(p)
        return -1
