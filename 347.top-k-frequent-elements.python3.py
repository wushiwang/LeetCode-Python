#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (50.13%)
# Total Accepted:    113.4K
# Total Submissions: 226.1K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
#
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
#


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = dict()
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        # Bucket Sort using frequency number in dic
        bucket = [set() for x in range(len(nums)+1)]
        for n in nums:
            bucket[dic[n]].add(n)
        res, i = [], 0
        for b in bucket[::-1]:
            for n in b:
                res.append(n)
                i += 1
                if i == k:
                    return res
