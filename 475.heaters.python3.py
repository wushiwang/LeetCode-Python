#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (29.81%)
# Total Accepted:    31.9K
# Total Submissions: 106.9K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
#
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
#
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
#
# Note:
#
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
#
#
#
# Example 1:
#
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
#
#
#
# Example 2:
#
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
#


class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if len(houses) == 0:
            return 0
        houses, heaters = sorted(houses), sorted(heaters)
        # (]
        L, R = -1, max(houses[-1], heaters[-1]) - houses[0]
        while L < R - 1:
            M = (L+R) >> 1
            if self.check(houses, heaters, M):
                R = M
            else:
                L = M
        return R

    def check(self, houses, heaters, r):
        h = [(x-r, x+r) for x in heaters]
        i = 0
        for t in houses:
            if t < h[i][0]:
                return False
            else:
                while i < len(h) and t > h[i][1]:
                    i += 1
                if i == len(h):
                    return False
                if t < h[i][0]:
                    return False
        return True
