#
# [465] Optimal Account Balancing
#
# https://leetcode.com/problems/optimal-account-balancing/description/
#
# algorithms
# Hard (39.63%)
# Total Accepted:    8.7K
# Total Submissions: 22.1K
# Testcase Example:  '[[0,1,10],[2,0,5]]'
#
# A group of friends went on holiday and sometimes lent each other money. For
# example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5
# for a taxi ride. We can model each transaction as a tuple (x, y, z) which
# means person x gave person y $z. Assuming Alice, Bill, and Chris are person
# 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can
# be represented as [[0, 1, 10], [2, 0, 5]].
#
# Given a list of transactions between a group of people, return the minimum
# number of transactions required to settle the debt.
#
# Note:
#
# A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
# Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we
# could also have the persons 0, 2, 6.
#
#
#
# Example 1:
#
# Input:
# [[0,1,10], [2,0,5]]
#
# Output:
# 2
#
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
#
# Two transactions are needed. One way to settle the debt is person #1 pays
# person #0 and #2 $5 each.
#
#
#
# Example 2:
#
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
#
# Output:
# 1
#
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
#
# Therefore, person #1 only need to give person #0 $4, and all debt is
# settled.
#
import math


class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        dic = dict()
        for x, y, v in transactions:
            if x not in dic:
                dic[x] = 0
            if y not in dic:
                dic[y] = 0
            dic[x] += v
            dic[y] -= v
        tmp = [v for k, v in dic.items()]
        A, B = list(filter(lambda x: x > 0, tmp)),\
            list(filter(lambda x: x < 0, tmp))
        self.dic = dict()
        return self.DFS(A, B)

    def DFS(self, A, B):
        if len(A) == 0:
            return 0
        s = str(A) + str(B)
        if s in self.dic:
            return self.dic[s]
        res = math.inf
        for i in range(len(B)):
            if B[i] + A[0] == 0:
                res = min(res, self.DFS(A[1:], B[:i]+B[i+1:])+1)
            elif B[i] + A[0] > 0:
                A[0] += B[i]
                res = min(res, self.DFS(A, B[:i]+B[i+1:])+1)
                A[0] -= B[i]
            else:
                B[i] += A[0]
                res = min(res, self.DFS(A[1:], B)+1)
                B[i] -= A[0]
        self.dic[s] = res
        return res
