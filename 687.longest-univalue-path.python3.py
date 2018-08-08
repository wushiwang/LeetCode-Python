#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (32.69%)
# Total Accepted:    32.4K
# Total Submissions: 99.1K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of
# edges between them.
#
#
# Example 1:
#
#
#
#
# Input:
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
#
#
# Output:
#
# 2
#
#
#
#
# Example 2:
#
#
#
#
# Input:
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
#
#
# Output:
#
# 2
#
#
#
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree
# is not more than 1000.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.DFS(root)
        return self.res

    def DFS(self, root):
        if root is None:
            return None, 0
        lv, lc = self.DFS(root.left)
        rv, rc = self.DFS(root.right)
        if root.val == lv == rv:
            self.res = max(self.res, lc+rc+2)
            c = max(lc, rc)+1
        elif root.val == lv:
            self.res = max(self.res, lc+1)
            c = lc+1
        elif root.val == rv:
            self.res = max(self.res, rc+1)
            c = rc+1
        else:
            c = 0
        return root.val, c
