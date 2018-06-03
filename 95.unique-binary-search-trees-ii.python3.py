
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (32.51%)
# Total Accepted:    103.8K
# Total Submissions: 319.2K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
# ⁠ 1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = [[None],
              [TreeNode(1)]]
        if n == 0:
            return []
        for i in range(2, n+1):
            a, b = 0, i-1
            dp.append([])
            for j in range(1, i+1):
                for x in dp[a]:
                    for y in dp[b]:
                        nt = TreeNode(j)
                        nt.left = x
                        nt.right = self.add(y, j)
                        dp[-1].append(nt)
                a, b = a + 1, b - 1
        return dp[n]

    def add(self, tn, v):
        if tn is None:
            return None
        nt = TreeNode(tn.val + v)
        nt.left = self.add(tn.left, v)
        nt.right = self.add(tn.right, v)
        return nt
