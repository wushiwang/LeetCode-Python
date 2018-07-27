#
# [593] Valid Square
#
# https://leetcode.com/problems/valid-square/description/
#
# algorithms
# Medium (39.86%)
# Total Accepted:    12.8K
# Total Submissions: 32.1K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# Given the coordinates of four points in 2D space, return whether the four
# points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two
# integers.
#
# Example:
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
#
#
#
# ⁠Note:
#
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
# Input points have no order.
#
import math


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        EPS = 1e-8
        points = list(set([tuple(p1), tuple(p2), tuple(p3), tuple(p4)]))
        if len(points) != 4:
            return False
        for i in range(4):
            cur = [0, 0]
            for j in range(4):
                for k in range(4):
                    if i != j and j != k and i != k:
                        v1 = (points[j][0]-points[i][0], points[j][1]-points[i][1])
                        v2 = (points[k][0]-points[i][0], points[k][1]-points[i][1])
                        cos = self.getCos(v1, v2)
                        if cos == 0:
                            cur[0] += 1
                        elif abs(cos - (1 / math.sqrt(2))) <= EPS:
                            cur[1] += 1
            if not (cur[0] == 2 and cur[1] == 4):
                return False
        return True

    def getCos(self, x, y):
        return (x[0]*y[0]+x[1]*y[1])/(math.sqrt(x[0]**2+x[1]**2)*math.sqrt(y[0]**2+y[1]**2))
