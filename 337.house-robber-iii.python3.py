#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (45.11%)
# Total Accepted:    69K
# Total Submissions: 153K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
#
#
#
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
#
#
# Example 1:
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \
# ⁠    3   1
#
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
#
# Example 2:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \
# ⁠1   3   1
#
# Maximum amount of money the thief can rob = 4 + 5 = 9.
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dic = dict()
        return self.DFS(root, True)

    def DFS(self, root, can):
        if root is None:
            return 0
        if (root, can) in self.dic:
            return self.dic[(root, can)]
        if can:
            res = max(root.val+self.DFS(root.left, False)+self.DFS(root.right, False),\
                    self.DFS(root.left, True)+self.DFS(root.right, True))
        else:
            res = self.DFS(root.left, True)+self.DFS(root.right, True)
        self.dic[(root, can)] = res
        return res
