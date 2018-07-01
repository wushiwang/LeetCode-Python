#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (60.74%)
# Total Accepted:    263.7K
# Total Submissions: 434.1K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
#
#
# Example:
# Given s = "hello", return "olleh".
#


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
