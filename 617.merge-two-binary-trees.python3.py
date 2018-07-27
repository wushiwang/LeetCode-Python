#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (68.07%)
# Total Accepted:    101.6K
# Total Submissions: 149.3K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
#
# Given two binary trees and imagine that when you put one of them to cover the
# other, some nodes of the two trees are overlapped while the others are
# not.
#
#
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
#
#
#
# Example 1:
#
# Input:
# Tree 1                     Tree 2
# ⁠         1                         2
# ⁠        / \                       / \
# ⁠       3   2                     1   3
# ⁠      /                           \   \
# ⁠     5                             4   7
# Output:
# Merged tree:
# 3
# / \
# 4   5
# / \   \
# 5   4   7
#
#
#
#
# Note:
# The merging process must start from the root nodes of both trees.
#


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.DFS(t1, t2)

    def DFS(self, root1, root2):
        if root1 is None and root2 is None:
            return
        elif root1 is None:
            val = root2.val
            L, R = self.DFS(None, root2.left), self.DFS(None, root2.right)
        elif root2 is None:
            val = root1.val
            L, R = self.DFS(root1.left, None), self.DFS(root1.right, None)
        else:
            val = root1.val + root2.val
            L, R = self.DFS(root1.left, root2.left), self.DFS(root1.right, root2.right)
        node = TreeNode(val)
        node.left, node.right = L, R
        return node
