#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (30.88%)
# Total Accepted:    25K
# Total Submissions: 81K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums, return the number of range sums that lie in
# [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j (i ≤ j), inclusive.
#
# Note:
# A naive algorithm of O(n2) is trivial. You MUST do better than that.
#
# Example:
#
#
# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective
# sums are: -2, -1, 2.
#


class Solution:
    class BIT:
        def __init__(self, n):
            self.bit = [0]*(n+1)

        def update(self, x, v):
            x += 1
            while x < len(self.bit):
                self.bit[x] += v
                x += x & (-x)

        def sum(self, x):
            x, res = x+1, 0
            while x > 0:
                res += self.bit[x]
                x -= x & (-x)
            return res

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # Pre processing
        sums, cur = {0}, 0
        for n in nums:
            cur += n
            sums.add(cur)
        sums = sorted(list(sums))
        index = {y: x for x, y in enumerate(sums)}
        # Calculate
        bit, res, cur = self.BIT(len(sums)), 0, 0
        bit.update(index[0], 1)
        for n in nums:
            cur += n
            L = self.bsGet(sums, cur - upper - 1)
            R = self.bsGet(sums, cur - lower)
            if L != -1 and R != -1:
                res += bit.sum(R)-bit.sum(L)
            elif L == -1 and R != -1:
                res += bit.sum(R)
            bit.update(index[cur], 1)
        return res

    def bsGet(self, nums, target):
        L, R = -1, len(nums)
        while L < R-1:
            M = (L+R) >> 1
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M
            else:
                R = M
        return L
