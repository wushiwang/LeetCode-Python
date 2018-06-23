#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (33.58%)
# Total Accepted:    77.9K
# Total Submissions: 231.9K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
#
# Note:  
#
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
#
# 1 2 3 4 5 6 8 9 10 12 15 16 27 30 32
# 1 2 4 6
# 1 3 6 9
# 1 5 10 15
import collections


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        l2, l3, l5 = collections.deque(), collections.deque(), collections.deque()
        l2.append(1)
        l3.append(1)
        l5.append(1)
        i = 1
        while i < n:
            cur = min(l2[0], l3[0], l5[0])
            if l2[0] == cur:
                l2.popleft()
            if l3[0] == cur:
                l3.popleft()
            if l5[0] == cur:
                l5.popleft()
            l2.append(cur*2)
            l3.append(cur*3)
            l5.append(cur*5)
            i += 1
        return min(l2[0], l3[0], l5[0])
