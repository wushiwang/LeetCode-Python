#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.65%)
# Total Accepted:    64.2K
# Total Submissions: 161.8K
# Testcase Example:  '[1,2,3,4,5]'
#
#
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
#
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1
# else return false.
#
#
#
# Your algorithm should run in O(n) time complexity and O(1) space
# complexity.
#
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
#
# Given [5, 4, 3, 2, 1],
# return false.
#
#
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
#


class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        tail = [nums[0]]
        for n in nums[1:]:
            if n > tail[-1]:
                tail.append(n)
            else:
                pos = 0
                while pos < len(tail) and tail[pos] < n:
                    pos += 1
                tail[pos] = n
            if len(tail) == 3:
                return True
        return False
