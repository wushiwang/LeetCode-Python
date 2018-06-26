#
# [293] Flip Game
#
# https://leetcode.com/problems/flip-game/description/
#
# algorithms
# Easy (57.45%)
# Total Accepted:    33.9K
# Total Submissions: 59K
# Testcase Example:  '"++++"'
#
# You are playing the following Flip Game with your friend: Given a string that
# contains only these two characters: + and -, you and your friend take turns
# to flip two consecutive "++" into "--". The game ends when a person can no
# longer make a move and therefore the other person will be the winner.
#
# Write a function to compute all possible states of the string after one valid
# move.
#
# Example:
#
#
# Input: s = "++++"
# Output:
# [
# ⁠ "--++",
# ⁠ "+--+",
# ⁠ "++--"
# ]
#
#
# Note: If there is no valid move, return an empty list [].
#


class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(1, len(s)):
            if s[i-1] == s[i] == '+':
                res.append(s[:i-1]+'--'+s[i+1:])
        return res
