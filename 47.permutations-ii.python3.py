#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (35.48%)
# Total Accepted:    167.4K
# Total Submissions: 471.3K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, visited = list(), [False for x in range(len(nums))]
        self.DFS(sorted(nums), 0, res, visited, list())
        return res

    def DFS(self, nums, n, res, visited, cur):
        if n == len(nums):
            res.append(cur)
            return
        i = 0
        while i < len(nums):
            if not visited[i]:
                visited[i] = True
                self.DFS(nums, n+1, res, visited, cur+[nums[i]])
                visited[i] = False
                while i != len(nums)-1 and nums[i] == nums[i+1]:
                    i += 1
            i += 1
