#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (30.55%)
# Total Accepted:    31K
# Total Submissions: 101.3K
# Testcase Example:  '8'
#
#
# Given a positive integer n and you can do operations as follow:
#
#
#
#
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
#
#
#
#
# What is the minimum number of replacements needed for n to become 1?
#
#
#
#
# Example 1:
#
# Input:
# 8
#
# Output:
# 3
#
# Explanation:
# 8 -> 4 -> 2 -> 1
#
#
#
# Example 2:
#
# Input:
# 7
#
# Output:
# 4
#
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
#


class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Special Case: N = 3
        # because 2 = 2**1, 4 = 2**2, N-1 = 2, N+1 = 4
        res = 0
        while n > 1:
            if n & 1 == 0:
                n >>= 1
            else:
                u, d = n+1, n-1
                if n != 3 and (u & (-u)) > (d & (-d)):
                    n += 1
                else:
                    n -= 1
            res += 1
        return res
