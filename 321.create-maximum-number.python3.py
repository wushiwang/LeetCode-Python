#
# [321] Create Maximum Number
#
# https://leetcode.com/problems/create-maximum-number/description/
#
# algorithms
# Hard (24.88%)
# Total Accepted:    24.5K
# Total Submissions: 98.3K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two. The
# relative order of the digits from the same array must be preserved. Return an
# array of the k digits.
#
# Note: You should try to optimize your time and space complexity.
#
# Example 1:
#
#
# Input:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]
#
# Example 2:
#
#
# Input:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# Output:
# [6, 7, 6, 0, 4]
#
# Example 3:
#
#
# Input:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# Output:
# [9, 8, 9]
#


class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(k+1):
            a, b = i, k-i
            if a <= len(nums1) and b <= len(nums2):
                res = max(res, self.merge(self.single(nums1, a), self.single(nums2, b)))
        return res

    def single(self, nums, k):
        res, pop = [], len(nums)-k
        for n in nums:
            while len(res) != 0 and res[-1] < n and pop > 0:
                res.pop()
                pop -= 1
            res.append(n)
        return res[:k]

    def merge(self, nums1, nums2):
        res = []
        while not (len(nums1) == 0 and len(nums2) == 0):
            if len(nums1) == 0:
                res += nums2
                break
            if len(nums2) == 0:
                res += nums1
                break
            if nums1 < nums2:
                res.append(nums2[0])
                nums2 = nums2[1:]
            else:
                res.append(nums1[0])
                nums1 = nums1[1:]
        return res
