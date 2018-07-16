#
# [480] Sliding Window Median
#
# https://leetcode.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (30.77%)
# Total Accepted:    15.3K
# Total Submissions: 49.7K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# Examples:
# [2,3,4] , the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position. Your
# job is to output the median array for each window in the original array.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
#
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7       -1
# ⁠1  3 [-1  -3  5] 3  6  7       -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
#
#
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
#
# Note:
# You may assume k is always valid, ie: k is always smaller than input array's
# size for non-empty array.
#
import bisect


class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window, res = [], []
        for i in range(len(nums)):
            if len(window) < k:
                bisect.insort(window, nums[i])
            else:
                res.append(self.getMedian(window))
                window.remove(nums[i-k])
                bisect.insort(window, nums[i])
        res.append(self.getMedian(window))
        return res

    def getMedian(self, nums):
        if len(nums) & 1 == 1:
            return float(nums[len(nums) >> 1])
        else:
            return (nums[(len(nums) >> 1)-1] + nums[len(nums) >> 1]) / 2.0
