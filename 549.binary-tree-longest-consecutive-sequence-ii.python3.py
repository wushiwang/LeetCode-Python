#
# [549] Binary Tree Longest Consecutive Sequence II
#
# algorithms
# Medium (42.78%)
# Total Accepted:    9.6K
# Total Submissions: 22.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given a binary tree, you need to find the length of Longest Consecutive Path
# in Binary Tree.
#
# Especially, this path can be either increasing or decreasing. For example,
# [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is
# not valid. On the other hand, the path can be in the child-Parent-child
# order, where not necessarily be parent-child order.
#
# Example 1:
#
# Input:
# ⁠       1
# ⁠      / \
# ⁠     2   3
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
#
#
#
# Example 2:
#
# Input:
# ⁠       2
# ⁠      / \
# ⁠     1   3
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
#
#
#
# Note:
# All the values of tree nodes are in the range of [-1e7, 1e7].
# ⁠
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
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.DFS(root)
        return self.res

    def DFS(self, root):
        if root is None:
            return 0, 0
        inc, dec = 0, 0
        if root.left is not None:
            linc, ldec = self.DFS(root.left)
            if root.left.val == root.val-1:
                inc = max(inc, linc)
            elif root.left.val == root.val+1:
                dec = max(dec, ldec)
        if root.right is not None:
            rinc, rdec = self.DFS(root.right)
            if root.right.val == root.val-1:
                inc = max(inc, rinc)
            elif root.right.val == root.val+1:
                dec = max(dec, rdec)
        self.res = max(self.res, inc+dec+1)
        return inc+1, dec+1
