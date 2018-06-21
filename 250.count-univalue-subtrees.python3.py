#
# [250] Count Univalue Subtrees
#
# https://leetcode.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (44.41%)
# Total Accepted:    23.7K
# Total Submissions: 53.5K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# Given a binary tree, count the number of uni-value subtrees.
#
# A Uni-value subtree means all nodes of the subtree have the same value.
#
# Example :
#
#
# Input:  root = [5,1,5,5,5,null,5]
#
# ⁠             5
# ⁠            / \
# ⁠           1   5
# ⁠          / \   \
# ⁠         5   5   5
#
# Output: 4
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
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.res = 0
        self.DFS(root)
        return self.res

    def DFS(self, root):
        if root.left is None and root.right is None:
            self.res += 1
            return True
        if root.left is not None and root.right is not None:
            L, R = self.DFS(root.left), self.DFS(root.right)
            if L and R and root.left.val == root.val and root.right.val == root.val:
                self.res += 1
                return True
        elif root.left is not None:
            L = self.DFS(root.left)
            if L and root.left.val == root.val:
                self.res += 1
                return True
        elif root.right is not None:
            R = self.DFS(root.right)
            if R and root.right.val == root.val:
                self.res += 1
                return True
        return False
