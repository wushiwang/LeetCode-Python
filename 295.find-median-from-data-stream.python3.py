#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (30.29%)
# Total Accepted:    63.8K
# Total Submissions: 210.6K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
#
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
#
# Design a data structure that supports the following two operations:
#
#
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
#
#
# Example:
#
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxx = []
        self.minn = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.maxx) == 0 or len(self.minn) == 0:
            heapq.heappush(self.maxx, -num)
        elif num < -self.maxx[0]:
            heapq.heappush(self.maxx, -num)
        else:
            heapq.heappush(self.minn, num)

        if len(self.maxx) - len(self.minn) == 2:
            heapq.heappush(self.minn, -heapq.heappop(self.maxx))
        elif len(self.minn) - len(self.maxx) == 2:
            heapq.heappush(self.maxx, -heapq.heappop(self.minn))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxx) == len(self.minn):
            return (self.minn[0]-self.maxx[0])/2
        elif len(self.maxx) > len(self.minn):
            return float(-self.maxx[0])
        else:
            return float(self.minn[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
