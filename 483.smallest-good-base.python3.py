#
# [483] Smallest Good Base
#
# https://leetcode.com/problems/smallest-good-base/description/
#
# algorithms
# Hard (34.00%)
# Total Accepted:    7.8K
# Total Submissions: 23.1K
# Testcase Example:  '"13"'
#
# For an integer n, we call k>=2 a good base of n, if all digits of n base k
# are 1.
# Now given a string representing n, you should return the smallest good base
# of n in string format.
#
# Example 1:
#
# Input: "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
#
#
#
# Example 2:
#
# Input: "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
#
#
#
# Example 3:
#
# Input: "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
#
#
#
# Note:
#
# The range of n is [3, 10^18].
# The string representing n is always valid and will not have leading zeros.
#


class Solution:
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        # ()
        n = int(n)
        res = n-1
        for i in range(1, 64):
            L, R = 1, n
            while L < R - 1:
                M = (L + R) >> 1
                c = self.check(n, M, i)
                if c == 1:
                    R = M
                elif c == -1:
                    L = M
                else:
                    res = min(res, M)
                    break
        return str(res)

    def check(self, n, x, m):
        p, cur = 1, 1
        for i in range(m-1):
            p *= x
            cur += p
        if cur < n:
            return -1
        elif cur > n:
            return 1
        else:
            return 0
