#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (37.09%)
# Total Accepted:    169.7K
# Total Submissions: 457.6K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
#
#
# The flattened tree should look like:
#
#
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        return

    def helper(self, root):
        if root is None:
            return None, None
        if root.left is None and root.right is None:
            return root, root

        H1, T1 = self.helper(root.left)
        H2, T2 = self.helper(root.right)
        if H1 is None:
            root.right = H2
            return root, T2
        if H2 is None:
            root.right = H1
            root.left = None
            return root, T1
        root.right = H1
        T1.right = H2
        root.left = None
        return root, T2
