#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (27.99%)
# Total Accepted:    80.8K
# Total Submissions: 288.5K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
#
# Note:
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Example:
#
#
# Input:
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
#
# Output: 6
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Get depth of tree
        k, cur = -1, root
        while cur:
            cur = cur.left
            k += 1
        if k == -1:
            return 0
        # Binary Search node nums, L, R -> [), O(lgn*lgn)
        L, R = 1 << k, 1 << (k+1)
        while L < R-1:
            M = (L + R) >> 1
            if self.check(root, k, M):
                L = M
            else:
                R = M
        return L

    def check(self, root, k, n):
        if root is None:
            return False
        if n == 1:
            return True
        if n - (1 << k) < (1 << (k-1)):
            return self.check(root.left, k-1, n - (1 << (k-1)))
        else:
            return self.check(root.right, k-1, n - (1 << k))
