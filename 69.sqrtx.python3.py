#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (29.05%)
# Total Accepted:    237.5K
# Total Submissions: 817K
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
# the decimal part is truncated, 2 is returned.
#


class Solution:
    def mySqrt(self, x):
        """
        :type x: int;
        :rtype: int
        """
        # [)
        L, R = 0, x + 1
        while L < R:
            M = (L + R) // 2
            tmp = M*M
            if tmp == x:
                return M
            elif tmp > x:
                R = M
            else:
                L = M + 1
        return L - 1
