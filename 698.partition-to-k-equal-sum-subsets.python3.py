#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (38.36%)
# Total Accepted:    18.9K
# Total Submissions: 49.3K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
#
# Example 1:
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
#
# Note:
# 1 .
# 0 < nums[i] < 10000.
#


class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0 or max(nums) > sum(nums) // k:
            return False
        target = sum(nums) // k
        nums = sorted(nums, reverse=True)
        self.visited = [False for _ in range(len(nums))]
        return self.DFS(k, 0, 0, target, nums)

    def DFS(self, k, pos, cur, target, nums):
        if k == 1:
            return True
        if cur == target:
            return self.DFS(k-1, 0, 0, target, nums)
        for i in range(pos, len(nums)):
            if cur + nums[i] <= target and not self.visited[i]:
                self.visited[i] = True
                if self.DFS(k, i, cur+nums[i], target, nums):
                    return True
                self.visited[i] = False
        return False
