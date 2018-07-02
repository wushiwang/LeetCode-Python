#
# [356] Line Reflection
#
# https://leetcode.com/problems/line-reflection/description/
#
# algorithms
# Medium (30.34%)
# Total Accepted:    15K
# Total Submissions: 49.4K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# Given n points on a 2D plane, find if there is such a line parallel to y-axis
# that reflect the given points.
#
#
# ⁠   Example 1:
#
#
# Given points = [[1,1],[-1,1]], return true.
#
#
#
# ⁠   Example 2:
#
#
# Given points = [[1,1],[-1,-1]], return false.
#
#
# Follow up:
# Could you do better than O(n2)?
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#


class Solution:
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points = set(map(lambda x: tuple(x), points))
        points = sorted(points, key=lambda x: (x[1], x[0]))
        dic = dict()
        for point in points:
            if point[1] not in dic:
                dic[point[1]] = []
            dic[point[1]].append(point[0])
        pre = None
        for y in dic:
            res, cur = self.check(dic[y])
            if not res or (pre != None and pre != cur):
                return False
            pre = cur
        return True

    def check(self, nums):
        L, R = 0, len(nums)-1
        pre = None
        while L <= R:
            cur = (nums[L]+nums[R]) / 2.0
            if pre != None and pre != cur:
                return False, None
            pre = cur
            L, R = L+1, R-1
        return True, pre
