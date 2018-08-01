#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (56.33%)
# Total Accepted:    52.3K
# Total Submissions: 92.8K
# Testcase Example:  '[3,9,20,15,7]'
#
# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.
#
# Example 1:
#
# Input:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level
# 2 is 11. Hence return [3, 14.5, 11].
#
#
#
# Note:
#
# The range of node's value is in the range of 32-bit signed integer.
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def avg(lst):
            return sum(lst) / len(lst)
        self.res = []
        self.DFS(root, 0)
        return list(map(avg, self.res))

    def DFS(self, root, level):
        if root is None:
            return
        if level == len(self.res):
            self.res.append([])
        self.res[level].append(root.val)
        self.DFS(root.left, level+1)
        self.DFS(root.right, level+1)
