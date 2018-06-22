#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (38.57%)
# Total Accepted:    59.5K
# Total Submissions: 154.3K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
#
# Example 1:
#
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
#
# Example 2:
#
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
#
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
#


class Solution:
    class UnionFind:
        def __init__(self, n):
            self.par = [x for x in range(n)]
            self.rank = [0 for x in range(n)]

        def union(self, a, b):
            x = self.find(a)
            y = self.find(b)
            if x == y:
                return False
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
            elif self.rank[x] < self.rank[y]:
                self.par[y] = x
            else:
                self.par[x] = y
                self.rank[y] += 1
            return True

        def find(self, a):
            if a != self.par[a]:
                self.par[a] = self.find(self.par[a])
            return self.par[a]

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        uf = self.UnionFind(n)
        for l, r in edges:
            if not uf.union(l, r):
                return False
        return True
