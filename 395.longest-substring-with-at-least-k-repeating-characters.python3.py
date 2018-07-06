#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (35.78%)
# Total Accepted:    27.6K
# Total Submissions: 77K
# Testcase Example:  '"aaabb"\n3'
#
#
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
#
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
#
#
#
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
#
import collections


class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        # 26 times two pointer
        # u means u unique characters shown at least k times
        res = 0
        for u in range(1, 27):
            if u*k > len(s):
                break
            dic, good = dict(), set()
            L, R, = 0, 0
            while R < len(s):
                if len(dic) < u:
                    if s[R] in dic:
                        dic[s[R]] += 1
                    else:
                        dic[s[R]] = 1
                    if dic[s[R]] >= k:
                        good.add(s[R])
                elif len(dic) == u:
                    if s[R] in dic:
                        dic[s[R]] += 1
                        if dic[s[R]] >= k:
                            good.add(s[R])
                    else:
                        dic[s[R]] = 1
                        while L < R and len(dic) > u:
                            dic[s[L]] -= 1
                            if s[L] in good and dic[s[L]] < k:
                                good.remove(s[L])
                            if dic[s[L]] == 0:
                                dic.pop(s[L])
                            L += 1
                R += 1
                if len(dic) == len(good):
                    res = max(res, R-L)
        return res
