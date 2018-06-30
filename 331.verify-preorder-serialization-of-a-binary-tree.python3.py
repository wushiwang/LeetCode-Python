#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (37.35%)
# Total Accepted:    47.2K
# Total Submissions: 126.4K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use pre-order traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as #.
#
#
# ⁠    _9_
# ⁠   /   \
# ⁠  3     2
# ⁠ / \   / \
# ⁠4   1  #  6
# / \ / \   / \
# # # # #   # #
#
#
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a correct
# preorder traversal serialization of a binary tree. Find an algorithm without
# reconstructing the tree.
#
# Each comma separated value in the string must be either an integer or a
# character '#' representing null pointer.
#
# You may assume that the input format is always valid, for example it could
# never contain two consecutive commas such as "1,,3".
#
# Example 1:
#
#
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
#
# Example 2:
#
#
# Input: "1,#"
# Output: false
#
#
# Example 3:
#
#
# Input: "9,#,#,1"
# Output: false
#


class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        nodes = preorder.split(',')
        if len(nodes) == 1 and nodes[0] == '#':
            return True
        for i in range(len(nodes)):
            node = nodes[i]
            if node == '#':
                if len(stack) == 0:
                    return False
                stack[-1] += 1
                while len(stack) != 0 and stack[-1] == 2:
                    stack.pop()
                    if len(stack) != 0:
                        stack[-1] += 1
                if len(stack) == 0 and i != len(nodes)-1:
                    return False
            else:
                stack.append(0)
        return len(stack) == 0
