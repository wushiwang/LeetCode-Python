#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (55.93%)
# Total Accepted:    44K
# Total Submissions: 78.7K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
#
# Example:
#
# Input:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \
# ⁠     5   3   9
#
# Output: [1, 3, 9]
#
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.DFS(root, 0)
        return self.res

    def DFS(self, root, level):
        if root is None:
            return
        if level == len(self.res):
            self.res.append(root.val)
        self.res[level] = max(self.res[level], root.val)
        self.DFS(root.left, level+1)
        self.DFS(root.right, level+1)
