#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (27.73%)
# Total Accepted:    9.1K
# Total Submissions: 32.8K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
#
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
#
# The given input is a directed graph that started as a rooted tree with N
# nodes (with distinct values 1, 2, ..., N), with one additional directed edge
# added.  The added edge has two different vertices chosen from 1 to N, and was
# not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
#
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of N nodes.  If there are multiple answers, return the answer that
# occurs last in the given 2D-array.
# Example 1:
#
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
#
#
# Example 2:
#
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5  2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4
#
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
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

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = self.UnionFind(len(edges))
        par = [None]*(len(edges)+1)
        ans1 = ans2 = None
        for i in range(len(edges)):
            u, v = edges[i]
            if par[v] is not None:
                ans1 = [par[v], v]
                ans2 = [u, v]
                edges[i] = None
            par[v] = u
        for i in range(len(edges)):
            if edges[i] is None:
                pass
            else:
                u, v = edges[i]
                if not uf.union(u, v):
                    if ans1 is not None:
                        return ans1
                    else:
                        return (u, v)
        return ans2
