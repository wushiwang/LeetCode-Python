#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (38.11%)
# Total Accepted:    17.7K
# Total Submissions: 46.4K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
#
# Two trees are duplicate if they have the same structure with same node
# values.
#
# Example 1:
#
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
#
#
# The following are two duplicate subtrees:
#
#
# ⁠     2
# ⁠    /
# ⁠   4
#
#
# and
#
#
# ⁠   4
#
# Therefore, you need to return above trees' root in the form of a list.
#


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.dic = dict()
        self.DFS(root)
        res = []
        for k, v in self.dic.items():
            if len(v) != 1:
                res.append(v[0])
        return res

    def DFS(self, root):
        if root is None:
            return ''
        s = str(root.val) + '(' + self.DFS(root.left) + ')(' + self.DFS(root.right) + ')'
        if s not in self.dic:
            self.dic[s] = []
        self.dic[s].append(root)
        return s
