#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (49.21%)
# Total Accepted:    52.3K
# Total Submissions: 106.3K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
# meetings.
#
# Example 1:
#
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
#
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: true
#
#
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key = lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True
