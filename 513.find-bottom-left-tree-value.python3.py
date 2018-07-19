#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (56.44%)
# Total Accepted:    49.3K
# Total Submissions: 87.3K
# Testcase Example:  '[2,1,3]'
#
#
# Given a binary tree, find the leftmost value in the last row of the tree.
#
#
# Example 1:
#
# Input:
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Output:
# 1
#
#
#
# ⁠ Example 2:
#
# Input:
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
#
# Output:
# 7
#
#
#
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        self.DFS(root, 0)
        return self.res[-1]

    def DFS(self, root, level):
        if root is None:
            return
        if level == len(self.res):
            self.res.append(root.val)
        self.DFS(root.left, level+1)
        self.DFS(root.right, level+1)
