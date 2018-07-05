#
# [391] Perfect Rectangle
#
# https://leetcode.com/problems/perfect-rectangle/description/
#
# algorithms
# Hard (27.55%)
# Total Accepted:    14.9K
# Total Submissions: 54.1K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
#
# Given N axis-aligned rectangles where N > 0, determine if they all together
# form an exact cover of a rectangular region.
#
#
#
# Each rectangle is represented as a bottom-left point and a top-right point.
# For example, a unit square is represented as [1,1,2,2]. (coordinate of
# bottom-left point is (1, 1) and top-right point is (2, 2)).
#
#
#
# Example 1:
#
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4],
# ⁠ [1,3,2,4],
# ⁠ [2,3,3,4]
# ]
#
# Return true. All 5 rectangles together form an exact cover of a rectangular
# region.
#
#
#
#
#
#
# Example 2:
#
# rectangles = [
# ⁠ [1,1,2,3],
# ⁠ [1,3,2,4],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4]
# ]
#
# Return false. Because there is a gap between the two rectangular
# regions.
#
#
#
#
#
#
# Example 3:
#
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [3,2,4,4]
# ]
#
# Return false. Because there is a gap in the top center.
#
#
#
#
#
#
# Example 4:
#
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [2,2,4,4]
# ]
#
# Return false. Because two of the rectangles overlap with each other.
#
#
import collections


class Solution:
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # 2 facts:
        # 1 -> Area of large rectangle  = Sum of area of little rectangles
        # 2 -> All points have shown even times, except 4 outer points of large
        # rectangle
        points, s = [], 0
        x, y, m, n = rectangles[0]
        for i in range(len(rectangles)):
            a, b, c, d = rectangles[i]
            x, y, m, n = min(x, a), min(y, b), max(m, c), max(n, d)
            s += (c-a)*(d-b)
            points += [(a, b), (a, d), (c, b), (c, d)]
        cnt, corner = collections.Counter(points), []
        for k in cnt:
            if cnt[k] & 1 == 1:
                if cnt[k] != 1:
                    return False
                else:
                    corner.append(k)
        if len(corner) != 4:
            return False
        corner = sorted(corner)
        if corner[0][0] == corner[1][0] == x and\
                corner[2][0] == corner[3][0] == m and\
                corner[0][1] == corner[2][1] == y and\
                corner[1][1] == corner[3][1] == n and\
                s == (m-x)*(n-y):
            return True
        return False
