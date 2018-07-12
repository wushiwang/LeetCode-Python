#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (41.16%)
# Total Accepted:    23.8K
# Total Submissions: 57.8K
# Testcase Example:  '[[1,2]]'
#
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
#
#
# Note:
#
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.
#
#
#
# Example 1:
#
# Input: [ [1,2], [2,3], [3,4], [1,3] ]
#
# Output: 1
#
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
#
#
#
# Example 2:
#
# Input: [ [1,2], [1,2], [1,2] ]
#
# Output: 2
#
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
#
#
#
# Example 3:
#
# Input: [ [1,2], [2,3] ]
#
# Output: 0
#
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
#
#
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start < stack[-1].end:
                if intervals[i].end < stack[-1].end:
                    stack.pop()
                    stack.append(intervals[i])
            else:
                stack.append(intervals[i])
        return len(intervals) - len(stack)
