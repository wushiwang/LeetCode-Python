#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (29.99%)
# Total Accepted:    37.5K
# Total Submissions: 125K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent plots - they
# would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
#
#
#
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
#
#
#
# Note:
#
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
#


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        res, i = 0, 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0 and i == len(flowerbed)-1:
                    res += 1
                    flowerbed[i] = 1
                elif i == 0:
                    if flowerbed[i+1] == 0:
                        res += 1
                        flowerbed[i] = 1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        res += 1
                        flowerbed[i] = 1
                elif flowerbed[i-1] == flowerbed[i+1] == 0:
                    res += 1
                    flowerbed[i] = 1
            i += 1
        return res >= n
