#
# [660] Remove 9
#
# https://leetcode.com/problems/remove-9/description/
#
# algorithms
# Hard (50.21%)
# Total Accepted:    4.2K
# Total Submissions: 8.4K
# Testcase Example:  '10'
#
# Start from integer 1, remove any integer that contains 9 such as 9, 19,
# 29...
#
# So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11,
# ...
#
# Given a positive integer n, you need to return the n-th integer after
# removing. Note that 1 will be the first integer.
#
# Example 1:
#
# Input: 9
# Output: 10
#
#
#
#
# ⁠Hint: n will not exceed 9 x 10^8.
#


class Solution:
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Just convert n to 9-based number
        base = 9
        res = ''
        while n != 0:
            res += str(n % 9)
            n //= 9
        return int(res[::-1])
