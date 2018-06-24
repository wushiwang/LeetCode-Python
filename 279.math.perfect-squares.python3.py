#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (38.01%)
# Total Accepted:    116.2K
# Total Submissions: 305.5K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
import math


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Based on Lagrange's Four Square theorem
        # Setp 1: If n is a perfect square number, result is 1
        tmp = math.floor(math.sqrt(n))
        if tmp*tmp == n:
            return 1
        # Step 2: For all numbers can be described as 4^k(8m+7), result is 4
        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4
        # Step 3: For all numbers can be described as x^2 + y^2, x, y != 0,
        # result is 2
        i = math.floor(math.sqrt(n))
        while i > 0:
            tmp = math.floor(math.sqrt(n-i*i))
            if tmp*tmp + i*i == n:
                return 2
            i -= 1
        # Step 4: For all other numbers, result is 3
        return 3
