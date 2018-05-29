#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.11%)
# Total Accepted:    154.4K
# Total Submissions: 530.7K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur_max = nums[len(nums)-1]
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] >= cur_max:
                cur_max = nums[i-1]
                j = i - 1
                while j + 1 != len(nums):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j = j + 1
            else:
                j = i
                while nums[j] <= nums[i-1]:
                    j = j + 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
        return
