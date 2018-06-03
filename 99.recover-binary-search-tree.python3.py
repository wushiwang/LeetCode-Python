#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (31.36%)
# Total Accepted:    90.2K
# Total Submissions: 287.6K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Example 1:
#
#
# Input: [1,3,null,null,2]
#
# 1
# /
# 3
# \
# 2
#
# Output: [3,1,null,null,2]
#
# 3
# /
# 1
# \
# 2
#
#
# Example 2:
#
#
# Input: [3,1,4,null,null,2]
#
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
#
# Output: [2,1,4,null,null,3]
#
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
#
#
# Follow up:
#
#
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.A, self.B, self.pre = None, None, None
        self.inner(root)
        self.A.val, self.B.val = self.B.val, self.A.val
        return

    def inner(self, root):
        if root is None:
            return
        self.inner(root.left)
        if self.pre is None:
            self.pre = root
        else:
            if self.pre.val > root.val:
                if self.A is None:
                    self.A = self.pre
                    self.B = root
                else:
                    self.B = root
            self.pre = root
        self.inner(root.right)
