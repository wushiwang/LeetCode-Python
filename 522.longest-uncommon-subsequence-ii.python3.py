#
# [522] Longest Uncommon Subsequence II
#
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/
#
# algorithms
# Medium (32.19%)
# Total Accepted:    12.5K
# Total Submissions: 38.9K
# Testcase Example:  '["aba","cdc","eae"]'
#
#
# Given a list of strings, you need to find the longest uncommon subsequence
# among them. The longest uncommon subsequence is defined as the longest
# subsequence of one of these strings and this subsequence should not be any
# subsequence of the other strings.
#
#
#
# A subsequence is a sequence that can be derived from one sequence by deleting
# some characters without changing the order of the remaining elements.
# Trivially, any string is a subsequence of itself and an empty string is a
# subsequence of any string.
#
#
#
# The input will be a list of strings, and the output needs to be the length of
# the longest uncommon subsequence. If the longest uncommon subsequence doesn't
# exist, return -1.
#
#
# Example 1:
#
# Input: "aba", "cdc", "eae"
# Output: 3
#
#
#
# Note:
#
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
#


class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = -1
        for i in range(len(strs)):
            flag = True
            for j in range(len(strs)):
                if i != j and self.check(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                res = max(res, len(strs[i]))
        return res

    def check(self, a, b):
        # Check a whether or not is b's subsequence
        if len(a) > len(b):
            return False
        if len(a) == len(b):
            return True if a == b else False
        L, R = 0, 0
        while L < len(a) and R < len(b):
            if a[L] == b[R]:
                L, R = L+1, R+1
            else:
                R += 1
        if L == len(a):
            return True
        return False
