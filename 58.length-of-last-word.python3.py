#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.08%)
# Total Accepted:    194.4K
# Total Submissions: 606K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space
# characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5
#


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp= list(s)
        i = len(tmp) - 1
        while i >= 0:
            if tmp[i] != " ":
                break
            i -= 1
        j = i
        while j >= 0:
            if tmp[j] == " ":
                break
            j -= 1
        return i - j
