#
# [266] Palindrome Permutation
#
# https://leetcode.com/problems/palindrome-permutation/description/
#
# algorithms
# Easy (58.32%)
# Total Accepted:    47.7K
# Total Submissions: 81.9K
# Testcase Example:  '"code"'
#
# Given a string, determine if a permutation of the string could form a
# palindrome.
#
# Example 1:
#
#
# Input: "code"
# Output: false
#
# Example 2:
#
#
# Input: "aab"
# Output: true
#
# Example 3:
#
#
# Input: "carerac"
# Output: true
#
import collections


class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt = collections.Counter(s)
        flag = False
        for k, v in cnt.items():
            if v%2 == 1:
                if flag:
                    return False
                flag = True
        return True
