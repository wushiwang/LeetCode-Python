#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (49.23%)
# Total Accepted:    39.2K
# Total Submissions: 79.6K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to find the number of connected
# components in an undirected graph.
#
# Example 1:
#
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4
#
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
#
# Output:  1
#
#
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
#


class Solution:
    class UnionFind:
        def __init__(self, n):
            self.par = [x for x in range(n)]
            self.rank = [0]*n

        def union(self, x, y):
            a, b = self.find(x), self.find(y)
            if a == b:
                return
            if self.rank[a] > self.rank[b]:
                self.par[a] = b
            elif self.rank[a] < self.rank[b]:
                self.par[b] = a
            else:
                self.par[b] = a
                self.rank[a] += 1

        def find(self, x):
            if self.par[x] != x:
                self.par[x] = self.find(self.par[x])
                self.rank[x] = 1
            return self.par[x]

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Union Find
        uf, res = self.UnionFind(n), n
        for l, r in edges:
            if uf.find(l) != uf.find(r):
                res -= 1
            uf.union(l, r)
        return res
