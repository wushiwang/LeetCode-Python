#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (50.34%)
# Total Accepted:    49.9K
# Total Submissions: 99.2K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
#
# Input:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
#
#
# Example 2:
#
# Input:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 28
#
# Output: False
#


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.root = root
        return self.DFS(root, k)

    def DFS(self, root, k):
        if root is None:
            return False
        m = k - root.val
        if self.find(self.root, m, root):
            return True
        return self.DFS(root.left, k) or self.DFS(root.right, k)

    def find(self, root, val, node):
        if root is None:
            return False
        if root.val == val and root != node:
            return True
        if val >= root.val:
            return self.find(root.right, val, node)
        if val <= root.val:
            return self.find(root.left, val, node)
