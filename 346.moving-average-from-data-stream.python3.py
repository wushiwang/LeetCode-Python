#
# [346] Moving Average from Data Stream
#
# https://leetcode.com/problems/moving-average-from-data-stream/description/
#
# algorithms
# Easy (60.93%)
# Total Accepted:    42.8K
# Total Submissions: 70.2K
# Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
#
# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.
#
# For example,
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
#
import collections


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.avg = 0.0
        self.s = 0.0
        self.size = size
        self.window = collections.deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.s += val
        self.window.append(val)
        if len(self.window) > self.size:
            self.s -= self.window.popleft()
        self.avg = self.s / len(self.window)
        return self.avg

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
