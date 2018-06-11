#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (25.45%)
# Total Accepted:    79.6K
# Total Submissions: 312.4K
# Testcase Example:  '[1,0,2]'
#
# There are N children standing in a line. Each child is assigned a rating
# value.
#
# You are giving candies to these children subjected to the following
# requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# What is the minimum candies you must give?
#
# Example 1:
#
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
#
#
# Example 2:
#
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# ⁠            The third child gets 1 candy because it satisfies the above two
# conditions.
#
import math


class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [0 for x in ratings]
        for i in range(len(ratings)):
            L = L + 1 if i-1 >= 0 and ratings[i] > ratings[i-1] else 1
            res[i] = L
        for i in range(len(ratings)-1, -1, -1):
            R = R + 1 if i+1 < len(ratings) and ratings[i] > ratings[i+1] else 1
            res[i] = max(res[i], R)
        return sum(res)
