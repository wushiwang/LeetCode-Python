#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.00%)
# Total Accepted:    36.9K
# Total Submissions: 122.9K
# Testcase Example:  '3'
#
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 231).
#
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
#
#
#
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
#


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, l = 1, 9
        while n > i*l:
            n -= i*l
            i, l = i+1, l*10
        num = ((n-1)//i) + 10**(i-1)
        return int(str(num)[(n-1)%i])
