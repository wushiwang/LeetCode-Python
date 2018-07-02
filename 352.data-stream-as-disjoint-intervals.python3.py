#
# [352] Data Stream as Disjoint Intervals
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (41.21%)
# Total Accepted:    18K
# Total Submissions: 43.6K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
# Given a data stream input of non-negative integers a1, a2, ..., an, ...,
# summarize the numbers seen so far as a list of disjoint intervals.
#
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6,
# ..., then the summary will be:
#
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
#
#
# Follow up:
# What if there are lots of merges and the number of disjoint intervals are
# small compared to the data stream's size?
#
#
# Credits:Special thanks to @yunhong for adding this problem and creating most
# of the test cases.
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ints = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        pos = self.__binarySearch(val)
        if pos == -1:
            self.ints = [Interval(val, val)] + self.ints
        else:
            if val == self.ints[pos].end+1:
                self.ints[pos].end += 1
            elif val > self.ints[pos].end+1:
                self.ints = self.ints[:pos+1] + [Interval(val, val)] + self.ints[pos+1:]
        for i in range(len(self.ints)-1):
            if self.ints[i].end == self.ints[i+1].start-1:
                self.ints[i].end = self.ints[i+1].end
                self.ints = self.ints[:i+1] + self.ints[i+2:]
                break

    def __binarySearch(self, val):
        L, R = -1, len(self.ints)
        while L < R - 1:
            M = (L+R) >> 1
            if self.ints[M].start <= val:
                L = M
            else:
                R = M
        return L

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.ints


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
