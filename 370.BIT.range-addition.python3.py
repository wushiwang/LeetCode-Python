#
# [370] Range Addition
#
# https://leetcode.com/problems/range-addition/description/
#
# algorithms
# Medium (57.44%)
# Total Accepted:    18.5K
# Total Submissions: 32.1K
# Testcase Example:  '5\n[[1,3,2],[2,4,3],[0,2,-2]]'
#
# Assume you have an array of length n initialized with all 0's and are given k
# update operations.
#
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which
# increments each element of subarray A[startIndex ... endIndex] (startIndex
# and endIndex inclusive) with inc.
#
# Return the modified array after all k operations were executed.
#
# Example:
#
# Given:
#
# ⁠   length = 5,
# ⁠   updates = [
# ⁠       [1,  3,  2],
# ⁠       [2,  4,  3],
# ⁠       [0,  2, -2]
# ⁠   ]
#
# Output:
#
# ⁠   [-2, 0, 3, 5, 3]
#
#
#
# Explanation:
#
# Initial state:
# [ 0, 0, 0, 0, 0 ]
#
# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]
#
# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]
#
# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]
#
#
#
# Credits:Special thanks to @vinod23 for adding this problem and creating all
# test cases.
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

    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # BIT --> range modification, single point query
        # Example:
        # for array A: 1 3 6 8 9
        # We build another array B: 1 2 3 2 1, which present A[i] - A[i-1]
        # Then range modification in A become single point modification in B
        # and single point query in A become range query in B
        # !!!
        bit = self.BIT(length)
        for l, r, v in updates:
            bit.update(l, v)
            bit.update(r+1, -v)
        res = []
        for i in range(length):
            res.append(bit.sum(i))
        return res
