#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (39.51%)
# Total Accepted:    113.9K
# Total Submissions: 288.1K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
#
#
# Example 1:
# Given s = "hello", return "holle".
#
#
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
#
#
# Note:
# The vowels does not include the letter "y".
#


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        tmp = ''.join(list(filter(lambda x: x in vowels, s))[::-1])
        res, i = '', 0
        for c in s:
            if c in vowels:
                res += tmp[i]
                i += 1
            else:
                res += c
        return res
