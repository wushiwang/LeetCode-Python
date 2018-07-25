#
# [573] Squirrel Simulation
#
# https://leetcode.com/problems/squirrel-simulation/description/
#
# algorithms
# Medium (52.61%)
# Total Accepted:    4.6K
# Total Submissions: 8.7K
# Testcase Example:  '5\n7\n[2,2]\n[4,4]\n[[3,0], [2,5]]'
#
# There's a tree, a squirrel, and several nuts. Positions are represented by
# the cells in a 2D grid. Your goal is to find the minimal distance for the
# squirrel to collect all the nuts and put them under the tree one by one. The
# squirrel can only take at most one nut at one time and can move in four
# directions - up, down, left and right, to the adjacent cell. The distance is
# represented by the number of moves.
#
# Example 1:
#
# Input:
# Height : 5
# Width : 7
# Tree position : [2,2]
# Squirrel : [4,4]
# Nuts : [[3,0], [2,5]]
# Output: 12
# Explanation:
#
#
#
#
# Note:
#
# All given positions won't overlap.
# The squirrel can take at most one nut at one time.
# The given positions of nuts have no order.
# Height and width are positive integers. 3
# The given positions contain at least one nut, only one tree and one
# squirrel.
#
import math


class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        first_pos, first_v = None, math.inf
        for i in range(len(nuts)):
            x = self.dis(nuts[i], tree)
            y = self.dis(nuts[i], squirrel)
            if y-x < first_v:
                first_v, first_pos = y-x, i
        res = 0
        for i in range(len(nuts)):
            if i != first_pos:
                res += self.dis(nuts[i], tree) * 2
        res += self.dis(nuts[first_pos], tree) + self.dis(nuts[first_pos], squirrel)
        return res

    def dis(self, x, y):
        return int(abs(x[0]-y[0])) + int(abs(x[1]-y[1]))
