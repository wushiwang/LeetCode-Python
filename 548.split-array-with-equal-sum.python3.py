#
# [548] Split Array with Equal Sum
#
# https://leetcode.com/problems/split-array-with-equal-sum/description/
#
# algorithms
# Medium (38.06%)
# Total Accepted:    4.5K
# Total Submissions: 11.9K
# Testcase Example:  '[1,2,1,2,1,2,1]'
#
#
# Given an array with n integers, you need to find if there are triplets  (i,
# j, k) which satisfies following conditions:
#
# ⁠0 < i, i + 1 < j, j + 1 < k < n - 1
# ⁠Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n -
# 1) should be equal.
#
# where we define that subarray (L, R) represents a slice of the original array
# starting from the element indexed L to the element indexed R.
#
#
# Example:
#
# Input: [1,2,1,2,1,2,1]
# Output: True
# Explanation:
# i = 1, j = 3, k = 5.
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
#
#
#
# Note:
#
# ⁠1
# ⁠Elements in the given array will be in range [-1,000,000, 1,000,000].
#


class Solution:
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False
        dup, i = [], 0
        # Optimization for TLE cases
        # ------------------------------------------------------------------
        while i < len(nums):
            zero = 0
            while i+1 < len(nums) and nums[i] == 0 and nums[i] == nums[i+1]:
                if zero <= 7:
                    dup.append(0)
                zero += 1
                i += 1
            if zero == 0:
                dup.append(nums[i])
            i += 1
        nums = dup
        # ------------------------------------------------------------------
        s, cur = [0]*len(nums), 0
        for i in range(len(nums)):
            cur += nums[i]
            s[i] = cur
        for j in range(3, len(nums)-3):
            cur = set()
            for i in range(1, len(nums)-5):
                if s[i-1] == s[j-1] - s[i]:
                    cur.add(s[i-1])
            if len(cur) == 0:
                continue
            for k in range(j+2, len(nums)-1):
                if s[k-1] - s[j] == s[-1] - s[k] and s[k-1] - s[j] in cur:
                    return True
        return False
