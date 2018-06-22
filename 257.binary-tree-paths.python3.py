#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (41.99%)
# Total Accepted:    165.9K
# Total Submissions: 395K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        res = []
        self.DFS(root, res, [])
        return res

    def DFS(self, root, res, cur):
        if root.left is None and root.right is None:
            res.append('->'.join(cur+[str(root.val)]))
            return
        if root.left is not None:
            self.DFS(root.left, res, cur+[str(root.val)])
        if root.right is not None:
            self.DFS(root.right, res, cur+[str(root.val)])
