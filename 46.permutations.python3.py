#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (47.95%)
# Total Accepted:    242.4K
# Total Submissions: 504.9K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, visited = list(), [False for x in range(len(nums))]
        self.DFS(nums, 0, res, visited, list())
        return res

    def DFS(self, nums, n, res, visited, cur):
        if n == len(nums):
            res.append(cur)
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                self.DFS(nums, n+1, res, visited, cur+[nums[i]])
                visited[i] = False
