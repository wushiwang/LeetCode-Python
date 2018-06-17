#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (25.35%)
# Total Accepted:    55.6K
# Total Submissions: 219.1K
# Testcase Example:  '"aacecaaa"'
#
# Given a string s, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
#
# Example 1:
#
#
# Input: "aacecaaa"
# Output: "aaacecaaa"
#
#
# Example 2:
#
#
# Input: "abcd"
# Output: "dcbabcd"
#
#
class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def __getLPS(p):
            '''
            Get LPS array for KMP algorithm
            '''
            lps, i, j = [-1 for x in range(len(p)+1)], 0, -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i, j = i + 1, j + 1
                    lps[i] = j
                else:
                    j = lps[j]
            return lps

        pos = (__getLPS(s+'#'+s[::-1])[-1])
        return s[pos:][::-1]+s
