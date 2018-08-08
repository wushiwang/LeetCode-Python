#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
#
# algorithms
# Hard (41.54%)
# Total Accepted:    14.4K
# Total Submissions: 34.6K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
#
# In a given array nums of positive integers, find three non-overlapping
# subarrays with maximum sum.
#
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k
# entries.
#
#
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed).  If there are multiple answers, return the
# lexicographically smallest one.
#
# Example:
#
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
# indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be
# lexicographically larger.
#
#
#
# Note:
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
#


class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = [[0]*len(nums) for _ in range(3)]
        s = [0]*len(nums)
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            s[i] = cur
        for i in range(3):
            for j in range(len(nums)):
                if j >= (i+1)*k-1:
                    ss = s[j]-s[j-k] if j-k >= 0 else s[j]
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-k]+ss)
        res, i, pre = [], 2, len(nums)-1
        while i >= 0:
            j = pre
            while dp[i][j] == dp[i][j-1]:
                j -= 1
            res.append(j-k+1)
            pre = j-k
            i -= 1
        return res[::-1]
