#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (39.70%)
# Total Accepted:    72.9K
# Total Submissions: 183.7K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
#
# Example 1:
#
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: 1
#
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda x: x.start)
        heap, res = [], 1
        heapq.heappush(heap, intervals[0].end)
        for i in range(1, len(intervals)):
            top = heap[0]
            if intervals[i].start >= top:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
            else:
                res += 1
                heapq.heappush(heap, intervals[i].end)
        return res
