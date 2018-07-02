#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (45.20%)
# Total Accepted:    18.6K
# Total Submissions: 41.2K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
#
# Given a sorted array of integers nums and integer values a, b and c.  Apply a
# quadratic function of the form f(x) = ax2 + bx + c to each element x in the
# array.
#
# The returned array must be in sorted order.
#
# Expected time complexity: O(n)
#
# Example:
#
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
#
# Result: [3, 9, 15, 33]
#
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
#
# Result: [-23, -5, 1, 7]
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x):
            return a*(x**2)+b*x+c
        if a > 0:
            # Find min value position
            minn = min(list(map(f, nums)))
            pos = 0
            for i in range(len(nums)):
                if f(nums[i]) == minn:
                    pos = i
                    break
            # Two pointer
            res = [minn]
            L, R = pos-1, pos+1
            while L >= 0 or R < len(nums):
                if L >= 0 and R < len(nums):
                    if f(nums[L]) < f(nums[R]):
                        res += [f(nums[L])]
                        L -= 1
                    else:
                        res += [f(nums[R])]
                        R += 1
                elif L >= 0:
                    res += [f(nums[L])]
                    L -= 1
                else:
                    res += [f(nums[R])]
                    R += 1
        else:
            maxx = max(list(map(f, nums)))
            pos = 0
            for i in range(len(nums)):
                if f(nums[i]) == maxx:
                    pos = i
                    break
            res = [maxx]
            L, R = pos-1, pos+1
            while L >= 0 or R < len(nums):
                if L >= 0 and R < len(nums):
                    if f(nums[L]) > f(nums[R]):
                        res += [f(nums[L])]
                        L -= 1
                    else:
                        res += [f(nums[R])]
                        R += 1
                elif L >= 0:
                    res += [f(nums[L])]
                    L -= 1
                else:
                    res += [f(nums[R])]
                    R += 1
            res = res[::-1]
        return res
