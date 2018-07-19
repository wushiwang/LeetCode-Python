#
# [517] Super Washing Machines
#
# https://leetcode.com/problems/super-washing-machines/description/
#
# algorithms
# Hard (36.48%)
# Total Accepted:    9.6K
# Total Submissions: 26.2K
# Testcase Example:  '[1,0,5]'
#
# You have n super washing machines on a line. Initially, each washing machine
# has some dresses or is empty.
#
#
# For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass
# one dress of each washing machine to one of its adjacent washing machines  at
# the same time .
#
# Given an integer array representing the number of dresses in each washing
# machine from left to right on the line, you should find the minimum number of
# moves to make all the washing machines have the same number of dresses. If it
# is not possible to do it, return -1.
#
# Example1
#
# Input: [1,0,5]
#
# Output: 3
#
# Explanation:
# 1st move:    1     0     1     1     4
# 2nd move:    1     2     1     3
# 3rd move:    2     1     2     2     2
#
#
# Example2
#
# Input: [0,3,0]
#
# Output: 2
#
# Explanation:
# 1st move:    0     1     2     0
# 2nd move:    1     2 --> 0    =>    1     1     1
#
#
# Example3
#
# Input: [0,2,0]
#
# Output: -1
#
# Explanation:
# It's impossible to make all the three washing machines have the same number
# of dresses.
#
#
#
#
# Note:
#
# The range of n is [1, 10000].
# The range of dresses number in a super washing machine is [0, 1e5].
#
# @see https://blog.csdn.net/tstsugeg/article/details/62427718


class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        s = [0]*(len(machines)+1)
        for i in range(len(machines)):
            s[i+1] = s[i] + machines[i]
        if s[-1] % len(machines) != 0:
            return -1
        target, res = s[-1] // len(machines), -1
        for i in range(len(machines)):
            L = s[i] - target*i
            R = s[-1] - s[i+1] - target*(len(machines)-i-1)
            if L < 0 and R < 0:
                res = max(res, -(L+R))
            elif L > 0 and R > 0:
                res = max(res, L, R)
            else:
                res = max(res, int(abs(L)), int(abs(R)))
        return res
