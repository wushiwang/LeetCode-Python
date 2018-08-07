#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (32.33%)
# Total Accepted:    37.1K
# Total Submissions: 114.8K
# Testcase Example:  '"aba"'
#
#
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
#
#
# Example 1:
#
# Input: "aba"
# Output: True
#
#
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
#
#
# Note:
#
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
#


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L, R, d = 0, len(s)-1, 0
        while L < R:
            if s[L] == s[R]:
                L, R = L+1, R-1
            else:
                if s[L+1] == s[R] and (L+2 >= len(s) or s[L+2] == s[R-1] or L == R-1):
                    L, d = L+1, d+1
                elif s[R-1] == s[L] and (R-2 < 0 or s[R-2] == s[L+1]):
                    R, d = R-1, d+1
                else:
                    return False
        return d <= 1
