#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (38.50%)
# Total Accepted:    144.6K
# Total Submissions: 375.5K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#


class UnionFind:
    def __init__(self, size):
        self.par = [x for x in range(size)]
        self.sz = [1 for x in range(size)]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.sz[a] < self.sz[b]:
            self.par[a] = b
            self.sz[b] += self.sz[a]
        else:
            self.par[b] = a
            self.sz[a] += self.sz[b]

    def find(self, a):
        if self.par[a] == a:
            return a
        self.par[a] = self.find(self.par[a])
        self.sz[a] = 1
        return self.par[a]

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def size(self, a):
        return self.sz[self.find(a)]


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        uf = UnionFind(len(nums))
        dic = dict(zip(nums, range(len(nums))))
        for n in nums:
            if n-1 not in dic:
                y = n + 1
                while y in dic:
                    uf.union(dic[n], dic[y])
                    y += 1

        return max(uf.sz)
