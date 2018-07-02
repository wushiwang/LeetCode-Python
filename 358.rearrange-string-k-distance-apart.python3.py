#
# [358] Rearrange String k Distance Apart
#
# https://leetcode.com/problems/rearrange-string-k-distance-apart/description/
#
# algorithms
# Hard (31.61%)
# Total Accepted:    15.4K
# Total Submissions: 48.8K
# Testcase Example:  '"aabbcc"\n3'
#
#
# Given a non-empty string s and an integer k, rearrange the string such that
# the same characters are at least distance k from each other.
#
#
# All input strings are given in lowercase letters. If it is not possible to
# rearrange the string, return an empty string "".
#
# Example 1:
#
# s = "aabbcc", k = 3
#
# Result: "abcabc"
#
# The same letters are at least distance 3 from each other.
#
#
#
# Example 2:
#
# s = "aaabc", k = 3
#
# Answer: ""
#
# It is not possible to rearrange the string.
#
#
#
# Example 3:
#
# s = "aaadbbcc", k = 2
#
# Answer: "abacabcd"
#
# Another possible answer is: "abcabcda"
#
# The same letters are at least distance 2 from each other.
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
import collections
import heapq


class Solution:
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cnt = collections.Counter(s)
        heap, rest = [], []
        for c, v in cnt.items():
            heapq.heappush(heap, (-v, c))
        res, i = '', 0
        while i < len(s) and len(heap) != 0:
            n, c = heapq.heappop(heap)
            n = -n - 1
            res += c
            if n != 0:
                if k <= 1:
                    heapq.heappush(heap, (-n, c))
                else:
                    heapq.heappush(rest, (i+k-1, n, c))
            if len(rest) > 0 and rest[0][0] == i:
                _, bn, bc = heapq.heappop(rest)
                heapq.heappush(heap, (-bn, bc))
            i += 1

        if i != len(s):
            return ''
        return res
