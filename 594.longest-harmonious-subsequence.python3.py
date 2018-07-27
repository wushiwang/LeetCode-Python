#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (41.42%)
# Total Accepted:    24.3K
# Total Submissions: 58.6K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# We define a harmonious array is an array where the difference between its
# maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest
# harmonious subsequence among all its possible subsequences.
#
# Example 1:
#
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#
#
#
# Note:
# The length of the input array will not exceed 20,000.
#
import collections


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        lst = sorted([(k, v) for k, v in cnt.items()])
        res = 0
        for i in range(1, len(lst)):
            if lst[i][0] - lst[i-1][0] == 1:
                res = max(res, lst[i-1][1] + lst[i][1])
        return res
