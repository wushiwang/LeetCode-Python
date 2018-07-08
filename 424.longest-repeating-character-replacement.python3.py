#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (42.47%)
# Total Accepted:    19.7K
# Total Submissions: 46.5K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string that consists of only uppercase English letters, you can
# replace any letter in the string with another letter at most k times. Find
# the length of a longest substring containing all repeating letters you can
# get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 104.
#
#
#
# Example 1:
#
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#
#
#
#
# Example 2:
#
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#


class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        L, R, res= 0, 0, 0
        num = [0 for x in range(26)]
        while R < len(s):
            num[ord(s[R]) - ord('A')] += 1
            maxx = max(num)
            while (R - L + 1) - maxx > k:
                num[ord(s[L]) - ord('A')] -= 1
                maxx = max(num)
                L += 1
            res = max(res, R-L+1)
            R += 1
        return res
