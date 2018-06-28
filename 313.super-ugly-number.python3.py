#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (38.60%)
# Total Accepted:    48.1K
# Total Submissions: 124.5K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
#
# Example:
#
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12
# ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
#
# Note:
#
#
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
#
import collections


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        lst = [collections.deque([1]) for x in range(len(primes))]
        i, res = 0, 0
        while i < n:
            cur = min([x[0] for x in lst])
            for j in range(len(primes)):
                lst[j].append(cur*primes[j])
                if lst[j][0] == cur:
                    lst[j].popleft()
            i += 1
            res = cur
        return res
