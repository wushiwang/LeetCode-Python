#
# [479] Largest Palindrome Product
#
# https://leetcode.com/problems/largest-palindrome-product/description/
#
# algorithms
# Easy (25.72%)
# Total Accepted:    11K
# Total Submissions: 42.9K
# Testcase Example:  '1'
#
# Find the largest palindrome made from the product of two n-digit numbers.
# ⁠Since the result could be very large, you should return the largest
# palindrome mod 1337.
#
# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
#
#
#
# Note:
# The range of n is [1,8].
#
import math


class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        if n & 1 == 0:
            s = '9'*(n//2) + '0'*(n//2)
            p = int(s + s[::-1])
            return p % 1337
        for a in range((10**n)-1, (10**(n-1))-1, -1):
            p = int(str(a)+str(a)[::-1])
            for b in range((10**n)-1, math.floor(math.sqrt(p))-1, -1):
                if p % b == 0:
                    if p // b > (10**n)-1:
                        break
                    return p % 1337
