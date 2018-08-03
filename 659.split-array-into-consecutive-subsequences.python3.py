#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (37.39%)
# Total Accepted:    10.4K
# Total Submissions: 27.9K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# You are given an integer array sorted in ascending order (may contain
# duplicates), you need to split them into several subsequences, where each
# subsequences consist of at least 3 consecutive integers. Return whether you
# can make such a split.
#
# Example 1:
#
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
#
#
#
# Example 2:
#
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
#
#
#
# Example 3:
#
# Input: [1,2,3,4,4,5]
# Output: False
#
#
#
# Note:
#
# The length of the input is in range of [1, 10000]
#
import collections


class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = collections.Counter(nums)
        nxt = collections.defaultdict(int)
        for n in nums:
            if cnt[n] > 0:
                if nxt[n] != 0:
                    nxt[n] -= 1
                    nxt[n+1] += 1
                elif cnt[n+1] > 0 and cnt[n+2] > 0:
                    nxt[n+3] += 1
                    cnt[n+1] -= 1
                    cnt[n+2] -= 1
                else:
                    return False
                cnt[n] -= 1
        return True
