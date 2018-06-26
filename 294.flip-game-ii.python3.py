#
# [294] Flip Game II
#
# https://leetcode.com/problems/flip-game-ii/description/
#
# algorithms
# Medium (47.11%)
# Total Accepted:    35.2K
# Total Submissions: 74.7K
# Testcase Example:  '"++++"'
#
# You are playing the following Flip Game with your friend: Given a string that
# contains only these two characters: + and -, you and your friend take turns
# to flip two consecutive "++" into "--". The game ends when a person can no
# longer make a move and therefore the other person will be the winner.
#
# Write a function to determine if the starting player can guarantee a win.
#
# Example:
#
#
# Input: s = "++++"
# Output: true
# Explanation: The starting player can guarantee a win by flipping the middle
# "++" to become "+--+".
#
#
# Follow up:
# Derive your algorithm's runtime complexity.
#
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# l w w w l w w w l w  w  w  w  w
# 9 -> 7, 6, 5, 4
# +++++++++ a
# ++++--+++ b
# --++--+++ a
# ------+++ b
# --------+ a


class Solution:
    def __init__(self):
        self.dic = dict()

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.dic:
            return self.dic[s]
        for i in range(1, len(s)):
            if s[i-1] == s[i] == '+':
                if not self.canWin(s[:i-1]+'--'+s[i+1:]):
                    self.dic[s] = True
                    return True
        self.dic[s] = False
        return False
