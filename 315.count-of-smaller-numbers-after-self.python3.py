#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (35.09%)
# Total Accepted:    50.4K
# Total Submissions: 143.5K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
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

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Binary Indexed Tree
        # Pre-processing
        dic, cnt = dict(), 0
        for n in sorted(nums):
            if n not in dic:
                dic[n] = cnt
                cnt += 1
        # Calculating
        bit = self.BIT(cnt)
        res = []
        for i in range(len(nums)-1, -1, -1):
            bit.update(dic[nums[i]], 1)
            res.append(bit.sum(dic[nums[i]]-1))
        return res[::-1]
