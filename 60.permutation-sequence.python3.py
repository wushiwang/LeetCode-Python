#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (29.77%)
# Total Accepted:    104.3K
# Total Submissions: 350.2K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# Given n and k, return the kth permutation sequence.
#
# Note:
#
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
import math


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        check, res, k = [str(x) for x in range(1, n+1)], "", k - 1
        tot = math.factorial(n)
        for i in range(n, 0, -1):
            cur = k//(tot//i)
            res += check[cur]
            check.pop(cur)
            k %= (tot//i)
            tot = tot//i

        return res
