#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.20%)
# Total Accepted:    95K
# Total Submissions: 625K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#
#
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import math
import collections


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        k = (y1-y2)/(x1-x2)
        b = y1-k*x1
        """
        points = [(i.x, i.y) for i in points]
        points = list(collections.Counter(points).items())
        if len(points) == 0:
            return 0
        res = max([i[1] for i in points])
        fixed = dict()
        for i in range(len(points)):
            dic = dict()
            for j in range(i+1, len(points)):
                x1, y1 = points[i][0][0], points[i][0][1]
                x2, y2 = points[j][0][0], points[j][0][1]
                k = (y1-y2)/(x1-x2) if x1-x2 != 0 else math.inf
                b = y1-k*x1 if x1-x2 != 0 else x1
                cur = (k, b)
                if cur not in fixed:
                    if cur not in dic:
                        dic[cur] = points[i][1] + points[j][1]
                    else:
                        dic[cur] += points[j][1]
                    res = max(res, dic[(k, b)])
            for d in dic:
                fixed[d] = dic[d]
        return res

