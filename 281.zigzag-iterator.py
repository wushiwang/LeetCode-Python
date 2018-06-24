#
# [281] Zigzag Iterator
#
# https://leetcode.com/problems/zigzag-iterator/description/
#
# algorithms
# Medium (53.07%)
# Total Accepted:    39.4K
# Total Submissions: 74.2K
# Testcase Example:  '[1,2]\n[3,4,5,6]'
#
# Given two 1d vectors, implement an iterator to return their elements
# alternately.
#
# Example:
#
#
# Input:
# v1 = [1,2]
# v2 = [3,4,5,6]
#
# Output: [1,3,2,4,5,6]
#
# Explanation: By calling next repeatedly until hasNext returns
# false,
# the order of elements returned by next should be: [1,3,2,4,5,6].
#
# Follow up: What if you are given k 1d vectors? How well can your code be
# extended to such cases?
#
# Clarification for the follow up question:
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
# If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For
# example:
#
#
# Input:
# [1,2,3]
# [4,5,6,7]
# [8,9]
#
# Output: [1,4,8,2,5,9,3,6,7].
#


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vec = [v1, v2]
        self.i_pos = 0
        self.j_pos = 0
        while self.i_pos < len(self.vec) and\
                self.j_pos >= len(self.vec[self.i_pos]):
            self.i_pos += 1

    def next(self):
        """
        :rtype: int
        """
        res = self.vec[self.i_pos][self.j_pos]
        self.i_pos += 1
        while self.i_pos < len(self.vec) and\
                self.j_pos >= len(self.vec[self.i_pos]):
            self.i_pos += 1
        if self.i_pos == len(self.vec):
            self.j_pos += 1
            self.i_pos = 0
        while self.i_pos < len(self.vec) and\
                self.j_pos >= len(self.vec[self.i_pos]):
            self.i_pos += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        for i in range(len(self.vec)):
            if self.j_pos < len(self.vec[i]):
                return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
