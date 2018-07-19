#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (52.54%)
# Total Accepted:    34.3K
# Total Submissions: 65.3K
# Testcase Example:  '[5,2,-3]'
#
#
# Given the root of a tree, you are asked to find the most frequent subtree
# sum. The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself). So
# what is the most frequent subtree sum value? If there is a tie, return all
# the values with the highest frequency in any order.
#
#
# Examples 1
# Input:
#
# ⁠ 5
# ⁠/  \
# 2   -3
#
# return [2, -3, 4], since all the values happen only once, return all of them
# in any order.
#
#
# Examples 2
# Input:
#
# ⁠ 5
# ⁠/  \
# 2   -5
#
# return [2], since 2 happens twice, however -5 only occur once.
#
#
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit
# signed integer.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.dic = dict()
        self.maxx = 0
        self.DFS(root)
        res = []
        for k, v in self.dic.items():
            if v == self.maxx:
                res.append(k)
        return res

    def DFS(self, root):
        if root.left is None and root.right is None:
            res = root.val
        elif root.left is None:
            res = root.val + self.DFS(root.right)
        elif root.right is None:
            res = root.val + self.DFS(root.left)
        else:
            res = root.val + self.DFS(root.left) + self.DFS(root.right)
        if res in self.dic:
            self.dic[res] += 1
        else:
            self.dic[res] = 1
        self.maxx = max(self.maxx, self.dic[res])
        return res
