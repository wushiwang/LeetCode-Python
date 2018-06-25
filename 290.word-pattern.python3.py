#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (33.65%)
# Total Accepted:    107.9K
# Total Submissions: 320.7K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
#
# Example 1:
#
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
#


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        ab = dict()
        ba = dict()
        for i in range(len(pattern)):
            if pattern[i] not in ab and str[i] not in ba:
                ab[pattern[i]] = str[i]
                ba[str[i]] = pattern[i]
            elif pattern[i] in ab and str[i] in ba and\
                    ab[pattern[i]] == str[i] and ba[str[i]] == pattern[i]:
                continue
            else:
                return False
        return True
