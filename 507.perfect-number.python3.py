#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (32.62%)
# Total Accepted:    26.4K
# Total Submissions: 80.9K
# Testcase Example:  '28'
#
# We define the Perfect Number is a positive integer that is equal to the sum
# of all its positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a
# perfect number and false when it is not.
#
#
# Example:
#
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
#
#
#
# Note:
# The input number n will not exceed 100,000,000. (1e8)
#
import math


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        res = 1
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                res += i + num // i
        return num == res
