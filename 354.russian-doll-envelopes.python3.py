#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (32.62%)
# Total Accepted:    30.9K
# Total Submissions: 94.8K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
#
#
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
#
#
# Example:
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes
# you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
#


class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0:
            return 0
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        tail = [envelopes[0][1]]
        for e in envelopes[1:]:
            if e[1] > tail[-1]:
                tail.append(e[1])
            elif e[1] < tail[0]:
                tail[0] = e[1]
            else:
                pos = self.binarySearch(tail, e[1])
                if pos != -1 and pos < len(tail):
                    tail[pos] = e[1]
        return len(tail)

    def binarySearch(self, tail, val):
        L, R = -1, len(tail)
        while L < R - 1:
            M = (L + R) >> 1
            if tail[M] >= val:
                R = M
            else:
                L = M
        return R
