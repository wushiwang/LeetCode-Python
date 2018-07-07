#
# [408] Valid Word Abbreviation
#
# https://leetcode.com/problems/valid-word-abbreviation/description/
#
# algorithms
# Easy (28.40%)
# Total Accepted:    16.9K
# Total Submissions: 59.6K
# Testcase Example:  '"internationalization"\n"i12iz4n"'
#
#
# Given a non-empty string s and an abbreviation abbr, return whether the
# string matches with the given abbreviation.
#
#
# A string such as "word" contains only the following valid abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#
#
# Notice that only the above abbreviations are valid abbreviations of the
# string "word". Any other string is not a valid abbreviation of "word".
#
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase
# letters and digits.
#
#
# Example 1:
#
# Given s = "internationalization", abbr = "i12iz4n":
#
# Return true.
#
#
#
# Example 2:
#
# Given s = "apple", abbr = "a2e":
#
# Return false.
#


class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, cur, lst, s = 0, '', [], 0
        while i < len(abbr):
            if ord(abbr[i]) >= ord('0') and ord(abbr[i]) <= ord('9'):
                cur += abbr[i]
            else:
                if cur != '':
                    if cur[0] == '0':
                        return False
                    s += int(cur)
                    lst.append(int(cur))
                    cur = ''
                s += 1
                lst.append(abbr[i])
            i += 1
        if cur != '':
            if cur[0] == '0':
                return False
            s += int(cur)
            lst.append(int(cur))
        if s != len(word):
            return False
        i, j = 0, 0
        while i < len(word) and j < len(lst):
            if type(lst[j]) is int:
                i, j = i+lst[j], j+1
            else:
                if word[i] != lst[j]:
                    return False
                i, j = i+1, j+1
        if i == len(word) and j == len(lst):
            return True
        return False
