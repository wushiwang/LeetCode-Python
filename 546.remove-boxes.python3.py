#
# [546] Remove Boxes
#
# https://leetcode.com/problems/remove-boxes/description/
#
# algorithms
# Hard (36.07%)
# Total Accepted:    6.6K
# Total Submissions: 18.3K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]'
#
# Given several boxes with different colors represented by different positive
# numbers.
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (composed
# of k boxes, k >= 1), remove them and get k*k points.
# Find the maximum points you can get.
#
#
# Example 1:
# Input:
#
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
#
# Output:
#
# 23
#
# Explanation:
#
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
#
#
#
# Note:
# The number of boxes n would not exceed 100.
#


class Solution:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        # Defination of i, j, k:
        # i, j: starting point and ending point of sub-list
        # k: how many left adjacent item equal to item boxes[i]
        self.dp = [[[0]*len(boxes) for x in range(len(boxes))] for y in range(len(boxes)+1)]
        return self.DFS(boxes, 0, len(boxes)-1, 1)

    def DFS(self, boxes, i, j, k):
        if i > j:
            return 0
        if i == j:
            return k*k
        if self.dp[i][j][k] != 0:
            return self.dp[i][j][k]
        # Import Optimization!! (avoid TLE)
        # Skip many recursions for test case like: 1,1,1,1,1,2,1,1,1
        while i+1 < j and boxes[i] == boxes[i+1]:
            i, k = i+1, k+1
        res = self.DFS(boxes, i+1, j, 1) + k*k
        for p in range(i+1, j+1):
            # Remove element boxes[p]
            if boxes[p] == boxes[i]:
                res = max(res, self.DFS(boxes, i+1, p-1, 1) + self.DFS(boxes, p, j, k+1))
        self.dp[i][j][k] = res
        return res
