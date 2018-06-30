#
# [333] Largest BST Subtree
#
# https://leetcode.com/problems/largest-bst-subtree/description/
#
# algorithms
# Medium (31.26%)
# Total Accepted:    22K
# Total Submissions: 70.4K
# Testcase Example:  '[10,5,15,1,8,null,7]'
#
# Given a binary tree, find the largest subtree which is a Binary Search Tree
# (BST), where largest means subtree with largest number of nodes in it.
# Note:
# A subtree must include all of its descendants.
# Here's an example:
#
# ⁠   10
# ⁠   / \
# ⁠  5  15
# ⁠ / \   \
# ⁠1   8   7
#
# The Largest BST Subtree in this case is the highlighted one.
# The return value is the subtree's size, which is 3.
#
#
#
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.DFS(root)
        return self.res

    def DFS(self, root):
        if root is None:
            return (True, 0, None, None)
        res1, s1, l1, r1 = self.DFS(root.left)
        res2, s2, l2, r2 = self.DFS(root.right)
        flag, l, r = False, None, None
        if res1 and res2:
            if root.left is not None and root.right is not None:
                if root.left.val < root.val and root.right.val > root.val and\
                        l2 > root.val and r1 < root.val:
                    flag = True
                    l, r = l1, r2
            elif root.left is not None:
                if root.left.val < root.val and r1 < root.val:
                    flag = True
                    l, r = l1, root.val
            elif root.right is not None:
                if root.right.val > root.val and l2 > root.val:
                    flag = True
                    l, r = root.val, r2
            else:
                flag = True
                l, r = root.val, root.val
        if flag:
            self.res = max(self.res, s1+s2+1)
        return flag, s1+s2+1, l, r
