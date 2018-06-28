#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (30.66%)
# Total Accepted:    42.3K
# Total Submissions: 137.8K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
#
# Example 1:
#
#
# Input: "bcabc"
# Output: "abc"
#
#
# Example 2:
#
#
# Input: "cbacdcbc"
# Output: "acdb"
#
import collections


class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Greedy
        if len(s) == 0:
            return ""
        cnt, pos = collections.Counter(s), 0
        for i in range(len(s)):
            if ord(s[i]) < ord(s[pos]):
                pos = i
            cnt[s[i]] -= 1
            if cnt[s[i]] == 0:
                return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))
