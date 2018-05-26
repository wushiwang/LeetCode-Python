#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.76%)
# Total Accepted:    495.2K
# Total Submissions: 2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        L, R, length = 0, 1, 1
        check_set = {s[0]}

        while R < len(s):
            if s[R] not in check_set:
                check_set.add(s[R])
            else:
                while s[L] != s[R]:
                    check_set.remove(s[L])
                    L = L + 1
                L = L + 1
            R = R + 1
            if (R - L) >= length:
                length = R - L
        return length
