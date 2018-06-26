#
# [296] Best Meeting Point
#
# https://leetcode.com/problems/best-meeting-point/description/
#
# algorithms
# Hard (52.51%)
# Total Accepted:    17.6K
# Total Submissions: 33.5K
# Testcase Example:  '[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# A group of two or more people wants to meet and minimize the total travel
# distance. You are given a 2D grid of values 0 or 1, where each 1 marks the
# home of someone in the group. The distance is calculated using Manhattan
# Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
#
# Example:
#
#
# Input:
#
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# Output: 6
#
# Explanation: Given three people living at (0,0), (0,4), and
# (2,2):
# The point (0,2) is an ideal meeting point, as the total travel
# distance
# of 2+2+2=6 is minimal. So return 6.
#


class Solution:
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        ones = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones.append((i, j))
        ones = sorted(ones, key=lambda x: x[0])
        a = ones[len(ones) >> 1][0]
        ones = sorted(ones, key=lambda x: x[1])
        b = ones[len(ones) >> 1][1]
        res = 0
        for one in ones:
            res += int(abs(a-one[0]))+int(abs(b-one[1]))
        return res
