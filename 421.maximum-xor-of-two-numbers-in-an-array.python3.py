#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (48.34%)
# Total Accepted:    24.9K
# Total Submissions: 51.5K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 231.
#
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
#
# Could you do this in O(n) runtime?
#
# Example:
#
# Input: [3, 10, 5, 25, 2, 8]
#
# Output: 28
#
# Explanation: The maximum result is 5 ^ 25 = 28.
#


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        res = 0
        cur = 1 << 31
        mask = 0x7fffffff
        for i in range(32):
            for n in nums:
                s.add(n | mask)
            for n in s:
                if (cur ^ n) in s:
                    res |= (1 << (31-i))
                    break
            if i != 31:
                cur = res | (1 << (31-i-1))
                mask >>= 1
            s.clear()
        return res
