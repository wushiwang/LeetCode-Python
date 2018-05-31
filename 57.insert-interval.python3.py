#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (29.17%)
# Total Accepted:    129.4K
# Total Submissions: 443.1K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their
# start times.
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res, flag = [], True
        for x in intervals:
            if flag and newInterval.start <= x.end:
                if newInterval.end < x.start:
                    res.append(newInterval)
                    res.append(x)
                else:
                    res.append(Interval(min(newInterval.start, x.start),
                                        max(newInterval.end, x.end)))
                flag = False
            else:
                if len(res) != 0 and x.start <= res[-1].end:
                    res[-1].end = max(res[-1].end, x.end)
                else:
                    res.append(x)
        if flag:
            res.append(newInterval)
        return res
