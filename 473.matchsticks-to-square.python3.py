#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (35.35%)
# Total Accepted:    17.5K
# Total Submissions: 49.4K
# Testcase Example:  '[1,1,2,2,2]'
#
# Remember the story of Little Match Girl? By now, you know exactly what
# matchsticks the little match girl has, please find out a way you can make one
# square by using up all those matchsticks. You should not break any stick, but
# you can link them up, and each matchstick must be used exactly one time.
#
# ⁠Your input will be several matchsticks the girl has, represented with their
# stick length. Your output will either be true or false, to represent whether
# you could make one square using all the matchsticks the little match girl
# has.
#
# Example 1:
#
# Input: [1,1,2,2,2]
# Output: true
#
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
#
#
#
# Example 2:
#
# Input: [3,3,3,3,4]
# Output: false
#
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
#
#
#
# Note:
#
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
#


class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        nums = sorted(nums, key=lambda x: -x)
        s = sum(nums)
        if s % 4 != 0 or nums[0] > s//4:
            return False
        res = [0, 0, 0, 0]
        return self.DFS(nums, 0, res, s//4)

    def DFS(self, nums, l, res, n):
        if l == len(nums):
            if res[0] == res[1] == res[2] == res[3] == n:
                return True
            return False
        cur = False
        for i in range(4):
            j = i-1
            while j >= 0:
                if res[j] == res[i]:
                    break
                j -= 1
            if j != -1:
                continue
            if res[i] + nums[l] <= n:
                res[i] += nums[l]
                cur = cur or self.DFS(nums, l+1, res, n)
                res[i] -= nums[l]
        return cur
