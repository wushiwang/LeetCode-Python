#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (47.17%)
# Total Accepted:    39.3K
# Total Submissions: 83.2K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
#


class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            a, dic = points[i], dict()
            for j in range(len(points)):
                b = points[j]
                dis = (a[0]-b[0])**2 + (a[1]-b[1])**2
                if dis not in dic:
                    dic[dis] = 0
                dic[dis] += 1
            for k in dic:
                if dic[k] >= 2:
                    res += dic[k] * (dic[k]-1) # P(n, 2) = n * (n-1)
        return res
