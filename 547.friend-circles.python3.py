#
# [547] Friend Circles
#
# https://leetcode.com/problems/friend-circles/description/
#
# algorithms
# Medium (49.52%)
# Total Accepted:    42.7K
# Total Submissions: 86.3K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
#
# There are N students in a class. Some of them are friends, while some are
# not. Their friendship is transitive in nature. For example, if A is a direct
# friend of B, and B is a direct friend of C, then A is an indirect friend of
# C. And we defined a friend circle is a group of students who are direct or
# indirect friends.
#
#
#
# Given a N*N matrix M representing the friend relationship between students in
# the class. If M[i][j] = 1, then the ith and jth students are direct friends
# with each other, otherwise not. And you have to output the total number of
# friend circles among all the students.
#
#
# Example 1:
#
# Input:
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a
# friend circle. The 2nd student himself is in a friend circle. So return 2.
#
#
#
# Example 2:
#
# Input:
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd
# students are direct friends, so the 0th and 2nd students are indirect
# friends. All of them are in the same friend circle, so return 1.
#
#
#
#
# Note:
#
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.
#


class Solution:
    class UnionFind:
        def __init__(self, n):
            self.par = [x for x in range(n)]
            self.rank = [0]*n

        def union(self, x, y):
            a, b = self.find(x), self.find(y)
            if a != b:
                if self.rank[a] > self.rank[b]:
                    self.par[b] = a
                elif self.rank[a] < self.rank[b]:
                    self.par[a] = b
                else:
                    self.par[a] = b
                    self.rank[b] += 1
                return True
            return False

        def find(self, x):
            if self.par[x] != x:
                self.par[x] = self.find(self.par[x])
                self.rank[x] = 1
            return self.par[x]

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        uf = self.UnionFind(len(M))
        res = len(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                if i != j and M[i][j] == 1:
                    if uf.union(i, j):
                        res -= 1
        return res
