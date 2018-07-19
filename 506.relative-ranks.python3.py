#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks/description/
#
# algorithms
# Easy (47.06%)
# Total Accepted:    32.7K
# Total Submissions: 69.5K
# Testcase Example:  '[5,4,3,2,1]'
#
#
# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".
#
# Example 1:
#
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so
# they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
# athletes, you just need to output their relative ranks according to their
# scores.
#
#
#
# Note:
#
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
#
#


class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tmp = sorted(nums, reverse=True)
        name = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        dic = dict()
        for i in range(min(len(nums), 3)):
            dic[tmp[i]] = name[i]
        for i in range(3, len(nums)):
            dic[tmp[i]] = str(i+1)
        res = []
        for i in range(len(nums)):
            res.append(dic[nums[i]])
        return res
