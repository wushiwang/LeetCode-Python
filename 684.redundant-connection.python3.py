#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (45.13%)
# Total Accepted:    20.4K
# Total Submissions: 45.1K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
#
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
#
# The given input is a graph that started as a tree with N nodes (with distinct
# values 1, 2, ..., N), with one additional edge added.  The added edge has two
# different vertices chosen from 1 to N, and was not an edge that already
# existed.
#
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] with u < v, that represents an undirected edge connecting
# nodes u and v.
#
# Return an edge that can be removed so that the resulting graph is a tree of N
# nodes.  If there are multiple answers, return the answer that occurs last in
# the given 2D-array.  The answer edge [u, v] should be in the same format,
# with u < v.
# Example 1:
#
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
# ⁠ 1
# ⁠/ \
# 2 - 3
#
#
# Example 2:
#
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
# ⁠   |   |
# ⁠   4 - 3
#
#
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
#
#
#
#
#
# Update (2017-09-26):
# We have overhauled the problem description + test cases and specified clearly
# the graph is an undirected graph. For the directed graph follow up please see
# Redundant Connection II). We apologize for any inconvenience caused.
#


class Solution:
    class UnionFind:
        def __init__(self, n):
            self.par = [x for x in range(n+1)]
            self.rank = [1]*(n+1)

        def union(self, x, y):
            a, b = self.find(x), self.find(y)
            if a != b:
                if self.rank[a] < self.rank[b]:
                    self.par[a] = b
                elif self.rank[b] < self.rank[a]:
                    self.par[b] = a
                else:
                    self.par[b] = a
                    self.rank[a] += 1
                return True
            return False

        def find(self, x):
            if x != self.par[x]:
                self.par[x] = self.find(self.par[x])
                self.rank[x] = 1
            return self.par[x]

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = self.UnionFind(len(edges))
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
