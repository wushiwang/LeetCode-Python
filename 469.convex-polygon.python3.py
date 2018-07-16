#
# [469] Convex Polygon
#
# https://leetcode.com/problems/convex-polygon/description/
#
# algorithms
# Medium (34.86%)
# Total Accepted:    5.9K
# Total Submissions: 16.8K
# Testcase Example:  '[[0,0],[0,1],[1,1],[1,0]]'
#
# Given a list of points that form a polygon when joined sequentially, find if
# this polygon is convex (Convex polygon definition).
#
# Note:
#
# There are at least 3 and at most 10,000 points.
# Coordinates are in the range -10,000 to 10,000.
# You may assume the polygon formed by given points is always a simple polygon
# (Simple polygon definition). In other words, we ensure that exactly two edges
# intersect at each vertex, and that edges otherwise don't intersect each
# other.
#
#
#
#
# Example 1:
#
# [[0,0],[0,1],[1,1],[1,0]]
#
# Answer: True
#
# Explanation:
#
#
#
# Example 2:
#
# [[0,0],[0,10],[10,10],[10,0],[5,5]]
#
# Answer: False
#
# Explanation:
#


class Solution:
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def cross(x, y):
            return x[0]*y[1] - y[0]*x[1]
        flag, last = True, 0
        points.append(points[0])
        points.append(points[1])
        for i in range(1, len(points)-1):
            x = (points[i][0]-points[i-1][0], points[i][1]-points[i-1][1])
            y = (points[i+1][0]-points[i-1][0], points[i+1][1]-points[i-1][1])
            cur = cross(x, y)
            if cur != 0:
                if cur*last < 0:
                    return False
                last = cur
        if flag and len(points) >= 5:
            return True
        return False
