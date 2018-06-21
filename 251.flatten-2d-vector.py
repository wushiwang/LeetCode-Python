#
# [251] Flatten 2D Vector
#
# https://leetcode.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (41.67%)
# Total Accepted:    38.5K
# Total Submissions: 92.3K
# Testcase Example:  '[[1,2],[3],[4,5,6]]'
#
# Implement an iterator to flatten a 2d vector.
#
# Example:
#
#
# Input: 2d vector =
# [
# ⁠ [1,2],
# ⁠ [3],
# ⁠ [4,5,6]
# ]
# Output: [1,2,3,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns
# false,
# the order of elements returned by next should be: [1,2,3,4,5,6].
#
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or
# iterators in Java.
#
#
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i, self.j = 0, 0
        while self.i < len(self.vec2d) and self.j == len(self.vec2d[self.i]):
                self.i += 1


    def next(self):
        """
        :rtype: int
        """
        res = self.vec2d[self.i][self.j]
        self.j += 1
        if self.j == len(self.vec2d[self.i]):
            self.j = 0
            self.i += 1
            while self.i < len(self.vec2d) and self.j == len(self.vec2d[self.i]):
                self.i += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.vec2d) == 0:
            return False
        return not (self.i == len(self.vec2d) and self.j == 0)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
