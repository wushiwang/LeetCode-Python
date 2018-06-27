#
# [305] Number of Islands II
#
# https://leetcode.com/problems/number-of-islands-ii/description/
#
# algorithms
# Hard (39.70%)
# Total Accepted:    35K
# Total Submissions: 88.2K
# Testcase Example:  '3\n3\n[[0,0],[0,1],[1,2],[2,1]]'
#
# A 2d grid map of m rows and n columns is initially filled with water. We may
# perform an addLand operation which turns the water at position (row, col)
# into a land. Given a list of positions to operate, count the number of
# islands after each addLand operation. An island is surrounded by water and is
# formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.
#
# Example:
#
#
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
#
#
# Explanation:
#
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water
# and 1 represents land).
#
#
# 0 0 0
# 0 0 0
# 0 0 0
#
#
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
#
#
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
#
#
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
#
#
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
#
#
# Follow up:
#
# Can you do it in time complexity O(k log mn), where k is the length of the
# positions?
#


class Solution:

    class UnionFind:
        def __init__(self):
            self.par = []
            self.rank = []

        def union(self, x, y):
            a, b = self.find(x), self.find(y)
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

        def add(self, x):
            self.par.append(x)
            self.rank.append(0)

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # Union Find
        dx = [1,0,0,-1]
        dy = [0,1,-1,0]
        uf = self.UnionFind()
        dic, cnt, res, tmp = dict(), 0, [], 0
        for x, y in positions:
            adj = set()
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if (nx, ny) in dic:
                    adj.add(uf.find(dic[(nx, ny)]))
            dic[(x, y)] = cnt
            uf.add(cnt)
            cnt += 1
            tmp -= (len(adj)-1)
            res.append(tmp)
            for v in adj:
                uf.union(cnt-1, v)
        return res
