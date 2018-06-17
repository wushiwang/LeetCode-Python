#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (41.35%)
# Total Accepted:    221.5K
# Total Submissions: 535.5K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
import random


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Quick Select (Quick sort)
        # Randomly generate pivot to avoid O(n^2) worst case)
        pivot = random.randint(0, len(nums)-1)
        nums[pivot], nums[-1] = nums[-1], nums[pivot]
        pivot, L = nums[-1], 0
        # Partition nums using pivot
        for i in range(len(nums)):
            if nums[i] > pivot:
                nums[L], nums[i] = nums[i], nums[L]
                L += 1
        nums[L], nums[-1] = nums[-1], nums[L]
        if L+1 == k:
            return nums[L]
        elif L+1 < k:
            return self.findKthLargest(nums[L+1:], k-L-1)
        else:
            return self.findKthLargest(nums[:L], k)
