#
# [657] Judge Route Circle
#
# https://leetcode.com/problems/judge-route-circle/description/
#
# algorithms
# Easy (68.78%)
# Total Accepted:    93.4K
# Total Submissions: 135.8K
# Testcase Example:  '"UD"'
#
#
# Initially, there is a Robot at position (0, 0). Given a sequence of its
# moves, judge if this robot makes a circle, which means it moves back to the
# original place.
#
#
#
# The move sequence is represented by a string. And each move is represent by a
# character. The valid robot moves are R (Right), L (Left), U (Up) and D
# (down). The output should be true or false representing whether the robot
# makes a circle.
#
#
# Example 1:
#
# Input: "UD"
# Output: true
#
#
#
# Example 2:
#
# Input: "LL"
# Output: false
#


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]
        d = {'U': 2,
             'D': 1,
             'L': 3,
             'R': 0}
        x, y = 0, 0
        for m in moves:
            nx, ny = x+dx[d[m]], y+dy[d[m]]
            x, y = nx, ny
        if nx == 0 and ny == 0:
            return True
        return False
