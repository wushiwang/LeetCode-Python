#
# [666] Path Sum IV
#
# https://leetcode.com/problems/path-sum-iv/description/
#
# algorithms
# Medium (50.77%)
# Total Accepted:    5.5K
# Total Submissions: 10.9K
# Testcase Example:  '[113,215,221]'
#
#
# If the depth of a tree is smaller than 5, then this tree can be represented
# by a list of three-digits integers.
#
#
#
# For each integer in this list:
#
# The hundreds digit represents the depth D of this node, 1
# The tens digit represents the position P of this node in the level it belongs
# to, 1 . The position is the same as that in a full binary tree.
# The units digit represents the value V of this node, 0
#
#
#
#
# Given a list of ascending three-digits integers representing a binary with
# the depth smaller than 5. You need to return the sum of all paths from the
# root towards the leaves.
#
#
# Example 1:
#
# Input: [113, 215, 221]
# Output: 12
# Explanation:
# The tree that the list represents is:
# ⁠   3
# ⁠  / \
# ⁠ 5   1
#
# The path sum is (3 + 5) + (3 + 1) = 12.
#
#
#
# Example 2:
#
# Input: [113, 221]
# Output: 4
# Explanation:
# The tree that the list represents is:
# ⁠   3
# ⁠    \
# ⁠     1
#
# The path sum is (3 + 1) = 4.
#


class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.tree = [None]*((2**5)-1)
        for n in nums:
            l, p, v = n//100, (n%100)//10, n%10
            pos = (2**(l-1)-1) + p - 1 if l != 1 else 0
            self.tree[pos] = v
        self.res = 0
        self.DFS(0, 0)
        return self.res

    def DFS(self, root, cur):
        if self.tree[root] is None:
            return
        cur += self.tree[root]
        left = root*2+1
        right = root*2+2
        if self.tree[left] is None and self.tree[right] is None:
            self.res += cur
        else:
            self.DFS(left, cur)
            self.DFS(right, cur)
