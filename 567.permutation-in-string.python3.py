#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (36.17%)
# Total Accepted:    24.6K
# Total Submissions: 68.1K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
#
# Example 1:
#
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
#
# Example 2:
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
#
#
# Note:
#
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
#
import collections


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cnt = collections.Counter(s1)
        L, R = 0, 0
        while R < len(s2):
            if cnt[s2[R]] != 0:
                cnt[s2[R]] -= 1
                R += 1
            else:
                while L <= R and cnt[s2[R]] == 0:
                    cnt[s2[L]] += 1
                    L += 1
                if cnt[s2[R]] == 0:
                    L, R = R+1, R+1
                else:
                    cnt[s2[R]] -= 1
                    R += 1
            if R-L == len(s1):
                return True
        return False
