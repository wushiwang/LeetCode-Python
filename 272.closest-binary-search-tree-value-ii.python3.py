#
# [272] Closest Binary Search Tree Value II
#
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
#
# algorithms
# Hard (40.49%)
# Total Accepted:    24.4K
# Total Submissions: 60.3K
# Testcase Example:  '[4,2,5,1,3]\n3.714286\n2'
#
# Given a non-empty binary search tree and a target value, find k values in the
# BST that are closest to the target.
#
# Note:
#
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that
# are closest to the target.
#
#
# Example:
#
#
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
#
# Output: [4,3]
#
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime
# (where n = total nodes)?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
import math


class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.res = collections.deque()
        self.inOrder(root, target, k)
        return list(self.res)

    def inOrder(self, root, target, k):
        if root is None:
            return
        self.inOrder(root.left, target, k)
        if len(self.res) < k:
            self.res.append(root.val)
        elif abs(target-root.val) < abs(target-self.res[0]):
            self.res.append(root.val)
            self.res.popleft()
        else:
            return
        self.inOrder(root.right, target, k)
