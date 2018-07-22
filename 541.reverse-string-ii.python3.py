#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (44.07%)
# Total Accepted:    43K
# Total Submissions: 97.5K
# Testcase Example:  '"abcdefg"\n2'
#
#
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k
# characters and left the other as original.
#
#
# Example:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#
#
#
# Restrictions:
#
# ⁠The string consists of lower English letters only.
# ⁠Length of the given string and k will in the range [1, 10000]
#


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left, i = len(s), 0
        res = ''
        while i < len(s):
            res += s[i:i+k][::-1] + s[i+k:i+2*k]
            i += 2*k
            left -= 2*k
        return res
