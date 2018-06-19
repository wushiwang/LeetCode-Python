#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (29.18%)
# Total Accepted:    35K
# Total Submissions: 120K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
#
#
# Input: 13
# Output: 6
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
#
# DP
# 923
# 923 -> 900 + 23 -> 899 + 23 -> 280 + 12 + 1 = 293
# 123
# 123 -> 99 + 24 + 23 -> 20 + 24 + 13 = 57
# 900 -> 999
# 0 -> 9, k = 1, 1
# 00 -> 99, k = 2, 10*1 + 10 = 20
# 000 -> 999, k = 3, 10*20 + 100 = 300
# 0000 -> 9999, k = 4, 10*300 + 1000 = 4000
# 101 -> 20 + 2 + 1 = 23

class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        k, tmp = 0, n
        while tmp != 0:
            k += 1
            tmp //= 10
        res, mask = 0, 10**(k-1)
        while n != 0:
            # Get left most digit
            cur = n // mask
            if cur == 1:
                res += (k-1)*(mask//10) + (n % mask) + 1
            else:
                res += cur*(k-1)*(mask//10) + mask
            n %= mask
            while n < mask:
                mask //= 10
                k -= 1
        return res
