#
# [715] Range Module
#
# https://leetcode.com/problems/range-module/description/
#
# algorithms
# Hard (31.00%)
# Total Accepted:    4.8K
# Total Submissions: 15.4K
# Testcase Example:  '["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]\n[[],[10,20],[14,16],[10,14],[13,15],[16,17]]'
#
# A Range Module is a module that tracks ranges of numbers. Your task is to
# design and implement the following interfaces in an efficient manner.
#
# addRange(int left, int right) Adds the half-open interval [left, right),
# tracking every real number in that interval.  Adding an interval that
# partially overlaps with currently tracked numbers should add any numbers in
# the interval [left, right) that are not already tracked.
#
# queryRange(int left, int right) Returns true if and only if every real number
# in the interval [left, right)
# ⁠is currently being tracked.
#
# removeRange(int left, int right) Stops tracking every real number currently
# being tracked in the interval [left, right).
#
# Example 1:
#
# addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true (Every number in [10, 14) is being tracked)
# queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not
# being tracked)
# queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked,
# despite the remove operation)
#
#
#
# Note:
# A half open interval [left, right) denotes all real numbers left .
#
# 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
# The total number of calls to addRange in a single test case is at most 1000.
# The total number of calls to queryRange in a single test case is at most
# 5000.
# The total number of calls to removeRange in a single test case is at most
# 1000.
#
import bisect


class RangeModule:

    def __init__(self):
        self.vec = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        L, R = bisect.bisect_left(self.vec, left), bisect.bisect_right(self.vec, right)
        if L & 1 == 1:
            L -= 1
            left = self.vec[L]
        if R & 1 == 1:
            right = self.vec[R]
            R += 1
        self.vec = self.vec[:L] + [left, right]  + self.vec[R:]


    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        L = bisect.bisect_right(self.vec, left)
        return L & 1 == 1 and L < len(self.vec) and self.vec[L-1] <= left < right <= self.vec[L]

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        L, R = bisect.bisect_left(self.vec, left), bisect.bisect_right(self.vec, right)
        new = []
        if L & 1 == 1:
            L -= 1
            new += [self.vec[L], left]
        if R & 1 == 1:
            new += [right, self.vec[R]]
            R += 1
        self.vec = self.vec[:L] + new + self.vec[R:]


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
