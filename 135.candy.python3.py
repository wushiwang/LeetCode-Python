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
        pq, candy = [(ratings[x], x) for x in range(len(ratings))], [-math.inf for x in range(len(ratings))]
        pq = sorted(pq, key=lambda x: x[0])
        res = 0
        for cur in pq:
            L, R = cur[1]-1, cur[1]+1
            maxx = max(candy[L] if L >= 0 and ratings[L] < ratings[cur[1]] else -math.inf,\
                       candy[R] if R < len(ratings) and ratings[R] < ratings[cur[1]] else -math.inf)
            if maxx == -math.inf:
                candy[cur[1]] = 1
                res += 1
            else:
                candy[cur[1]] = maxx + 1
                res += maxx + 1
        return res
