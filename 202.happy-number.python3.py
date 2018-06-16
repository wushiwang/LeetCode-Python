#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (42.00%)
# Total Accepted:    168K
# Total Submissions: 399.8K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
#
# Example: 
#
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = set()
        while n != 1:
            if n in dic:
                return False
            else:
                dic.add(n)
            s = 0
            while n != 0:
                s += (n%10)**2
                n //= 10
            n = s
        return True
