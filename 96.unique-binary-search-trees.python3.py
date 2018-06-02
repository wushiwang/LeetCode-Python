#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (42.26%)
# Total Accepted:    152.2K
# Total Submissions: 360.1K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0 for x in range(n+1)]
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(i>>1):
                dp[i] += dp[j]*dp[i-1-j]
            dp[i] *= 2
            if i & 1 == 1:
                dp[i] += dp[i>>1]*dp[i>>1]
        return dp[n]
