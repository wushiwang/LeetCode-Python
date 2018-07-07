#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (46.16%)
# Total Accepted:    68.7K
# Total Submissions: 148.8K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
import collections


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.Counter(s)
        res, flag = 0, False
        for k in cnt:
            if cnt[k] & 1 == 0:
                res += cnt[k]
            else:
                flag = True
                res += cnt[k]-1
        return res+1 if flag else res
