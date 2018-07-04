#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (47.94%)
# Total Accepted:    83.7K
# Total Submissions: 174.4K
# Testcase Example:  '"a"\n"b"'
#
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return
# false.
#
#
# Each letter in the magazine string can only be used once in your ransom
# note.
#
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#
import collections


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt_note, cnt_mag = collections.Counter(ransomNote), collections.Counter(magazine)
        for k in cnt_note:
            if cnt_mag[k] < cnt_note[k]:
                return False
        return True
