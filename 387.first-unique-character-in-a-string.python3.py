#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (47.30%)
# Total Accepted:    138.5K
# Total Submissions: 292.7K
# Testcase Example:  '"leetcode"'
#
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#
import collections


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.Counter(s)
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1
