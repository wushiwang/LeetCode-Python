#
# [679] 24 Game
#
# https://leetcode.com/problems/24-game/description/
#
# algorithms
# Hard (38.95%)
# Total Accepted:    9.7K
# Total Submissions: 24.9K
# Testcase Example:  '[4,1,8,7]'
#
#
# You have 4 cards each containing a number from 1 to 9.  You need to judge
# whether they could operated through *, /, +, -, (, ) to get the value of
# 24.
#
#
# Example 1:
#
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#
#
#
# Example 2:
#
# Input: [1, 2, 1, 2]
# Output: False
#
#
#
# Note:
#
# The division operator / represents real division, not integer division.  For
# example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use -
# as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression
# -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2,
# 1, 2], we cannot write this as 12 + 12.
#
import itertools
import operator


class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.ops = [operator.add,
                    operator.sub,
                    operator.mul,
                    operator.truediv]
        for cur in itertools.permutations(nums):
            if self.DFS(list(cur)):
                return True
        return False

    def DFS(self, nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) <= 1e-5
        for i in range(len(nums)-1):
            a, b = nums[i], nums[i+1]
            for o in range(4):
                if o <= 2 or(o == 3 and b != 0):
                    cur = self.ops[o](a, b)
                    if self.DFS(nums[:i]+[cur]+nums[i+2:]):
                        return True
        return False
