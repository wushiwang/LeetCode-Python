#
# [311] Sparse Matrix Multiplication
#
# https://leetcode.com/problems/sparse-matrix-multiplication/description/
#
# algorithms
# Medium (52.78%)
# Total Accepted:    48.4K
# Total Submissions: 91.8K
# Testcase Example:  '[[1,0,0],[-1,0,3]]\n[[7,0,0],[0,0,0],[0,0,1]]'
#
# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
#
# Input:
#
# A = [
# ⁠ [ 1, 0, 0],
# ⁠ [-1, 0, 3]
# ]
#
# B = [
# ⁠ [ 7, 0, 0 ],
# ⁠ [ 0, 0, 0 ],
# ⁠ [ 0, 0, 1 ]
# ]
#
# Output:
#
# ⁠    |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
# ⁠                 | 0 0 1 |
#


class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A == []:
            return []
        # Preprocessing
        nA = []
        for i in range(len(A)):
            tmp = []
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    tmp.append((A[i][j], j))
            nA.append(tmp)
        # Calculating
        res = []
        for i in range(len(nA)):
            cur = []
            for j in range(len(B[0])):
                s = 0
                for v, p in nA[i]:
                    s += v*B[p][j]
                cur.append(s)
            res.append(cur)
        return res
