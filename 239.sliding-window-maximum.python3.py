#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (34.49%)
# Total Accepted:    94.3K
# Total Submissions: 273.3K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Example:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
#
# Follow up:
# Could you solve it in linear time?
#
import collections


class Solution:
    class MonotonicQueue:
        """
        Descending Monotonic Queue
        """
        def __init__(self):
            self.q = collections.deque()

        def push(self, x):
            while len(self.q) != 0 and self.q[-1] < x:
                self.q.pop()
            self.q.append(x)

        def pop(self):
            self.q.popleft()

        def max(self):
            return self.q[0]

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        mq = self.MonotonicQueue()
        for i in range(0, k):
            mq.push(nums[i])
        res = [mq.max()]
        for i in range(k, len(nums)):
            if nums[i-k] == mq.max():
                mq.pop()
            mq.push(nums[i])
            res.append(mq.max())
        return res
