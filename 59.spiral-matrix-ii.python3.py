#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (41.47%)
# Total Accepted:    103.1K
# Total Submissions: 248.3K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res = [[0 for x in range(n)] for y in range(n)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        i, j, cur, res[0][0], visited = 0, 0, 2, 1, {(0, 0): True}
        while True:
            for x in range(4):
                while i + dx[x] >= 0 and i + dx[x] < n and\
                        j + dy[x] >= 0 and j + dy[x] < n and\
                        (i+dx[x], j+dy[x]) not in visited:
                    res[i+dx[x]][j+dy[x]], cur = cur, cur + 1
                    visited[(i+dx[x], j+dy[x])] = True
                    i, j = i+dx[x], j+dy[x]
            if cur > n*n:
                return res
