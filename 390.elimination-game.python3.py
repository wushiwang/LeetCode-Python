#
# [390] Elimination Game
#
# https://leetcode.com/problems/elimination-game/description/
#
# algorithms
# Medium (42.77%)
# Total Accepted:    17.7K
# Total Submissions: 41.5K
# Testcase Example:  '9'
#
#
# There is a list of sorted integers from 1 to n. Starting from left to right,
# remove the first number and every other number afterward until you reach the
# end of the list.
#
# Repeat the previous step again, but this time from right to left, remove the
# right most number and every other number from the remaining numbers.
#
# We keep repeating the steps again, alternating left to right and right to
# left, until a single number remains.
#
# Find the last number that remains starting with a list of length n.
#
# Example:
#
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
#
# Output:
# 6
# 1 2
# 2
# 1 2 3
# 2
# 1 2 3 4
# 2
# 1 2 3 4 5
# 2
# 1 2 3 4 5 6
# 4
# 1 2 3 4 5 6 7
# 4
# 6
# 6
# 8
# 8
# 6

class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n) + 1

    def helper(self, n):
        if n <= 2:
            return n-1
        if n & 1 == 1:
            return self.helper(n-1)
        else:
            return n-1-2*self.helper(n//2)
