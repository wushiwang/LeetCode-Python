#
# [667] Beautiful Arrangement II
#
# https://leetcode.com/problems/beautiful-arrangement-ii/description/
#
# algorithms
# Medium (50.92%)
# Total Accepted:    12.6K
# Total Submissions: 24.7K
# Testcase Example:  '3\n2'
#
#
# Given two integers n and k, you need to construct a list which contains n
# different positive integers ranging from 1 to n and obeys the following
# requirement:
#
# Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 -
# a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
#
#
#
# If there are multiple answers, print any of them.
#
#
# Example 1:
#
# Input: n = 3, k = 1
# Output: [1, 2, 3]
# Explanation: The [1, 2, 3] has three different positive integers ranging from
# 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
#
#
#
# Example 2:
#
# Input: n = 3, k = 2
# Output: [1, 3, 2]
# Explanation: The [1, 3, 2] has three different positive integers ranging from
# 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
#
#
#
# Note:
#
# The n and k are in the range 1 4.
#


class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        used = [False]*(n+1)
        res, cur = [1], 1
        used[1] = True
        while k != 0:
            nxt = cur+k if len(res)&1 == 1 else cur-k
            res.append(nxt)
            used[nxt] = True
            cur = nxt
            k -= 1
        for i in range(1, n+1):
            if not used[i]:
                res.append(i)
        return res
