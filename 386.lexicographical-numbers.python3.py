#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (42.69%)
# Total Accepted:    30.3K
# Total Submissions: 71.1K
# Testcase Example:  '13'
#
#
# Given an integer n, return 1 - n in lexicographical order.
#
#
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
#
#
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
#


class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, 10):
            if i <= n:
                self.DFS(i, res, n)
        return res

    def DFS(self, cur, res, n):
        res.append(cur)
        for i in range(0, 10):
            nxt = cur*10+i
            if nxt <= n:
                self.DFS(cur*10+i, res, n)
