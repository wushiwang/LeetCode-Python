#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (27.13%)
# Total Accepted:    151.3K
# Total Submissions: 557.9K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
#


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if len(t) == 0:
            return s[0]
        tar, res = {}, ""
        for c in t:
            if c in tar:
                tar[c] += 1
            else:
                tar[c] = 1
        L, R, cur = 0, 0, 0
        while R < len(s):
            if s[L] not in tar:
                while L < len(s) and s[L] not in tar:
                    L += 1
                R = L
                continue
            if s[R] in tar:
                if tar[s[R]] > 0:
                    cur += 1
                tar[s[R]] -= 1
                while tar[s[L]] < 0:
                    tar[s[L]] += 1
                    L += 1
                    while L < len(s) and s[L] not in tar:
                        L += 1
                if cur == len(t):
                    if len(res) == 0 or len(res) > R - L + 1:
                        res = s[L:R+1]
            R += 1
        return res
