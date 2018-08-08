#
# [683] K Empty Slots
#
# https://leetcode.com/problems/k-empty-slots/description/
#
# algorithms
# Hard (33.55%)
# Total Accepted:    17.4K
# Total Submissions: 52K
# Testcase Example:  '[1,3,2]\n1'
#
#
# There is a garden with N slots. In each slot, there is a flower. The N
# flowers will bloom one by one in N days. In each day, there will be exactly
# one flower blooming and it will be in the status of blooming since then.
#
#
#
# Given an array flowers consists of number from 1 to N. Each number in the
# array represents the place where the flower will open in that day.
#
#
#
# For example, flowers[i] = x means that the unique flower that blooms at day i
# will be at position x, where i and x will be in the range from 1 to N.
#
#
#
# Also given an integer k, you need to output in which day there exists two
# flowers in the status of blooming, and also the number of flowers between
# them is k and these flowers are not blooming.
#
#
#
# If there isn't such day, output -1.
#
#
# Example 1:
#
# Input:
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become
# blooming.
#
#
#
# Example 2:
#
# Input:
# flowers: [1,2,3]
# k: 1
# Output: -1
#
#
#
#
# Note:
#
# The given array will be in the range [1, 20000].
#
import math


class Solution:
    class bucket:
        def __init__(self):
            self.max = -1
            self.min = math.inf

    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        # bucket length: k+1
        b = [self.bucket() for _ in range(math.ceil(len(flowers) / (k+1)))]
        for i in range(len(flowers)):
            cur = flowers[i]-1
            pos = (cur) // (k+1)
            if cur > b[pos].max:
                b[pos].max = cur
                if pos != len(b)-1 and b[pos+1].min == cur+k+1:
                    return i+1
            if cur < b[pos].min:
                b[pos].min = cur
                if pos != 0 and b[pos-1].max == cur-k-1:
                    return i+1
        return -1
