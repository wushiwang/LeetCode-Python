#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (26.64%)
# Total Accepted:    161.6K
# Total Submissions: 606.5K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
import math


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        isPrime = [True for x in range(n)]
        up, res = math.floor(math.sqrt(n-1)), 0
        for i in range(2, up+1):
            if isPrime[i]:
                res += 1
                j = i*2
                while j < n:
                    isPrime[j] = False
                    j += i
        for i in range(up+1, n):
            if isPrime[i]:
                res += 1
        return res
