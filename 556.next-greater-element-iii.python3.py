#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (28.84%)
# Total Accepted:    15.2K
# Total Submissions: 52.7K
# Testcase Example:  '12'
#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer n and is
# greater in value than n. If no such positive 32-bit integer exists, you need
# to return -1.
#
# Example 1:
#
#
# Input: 12
# Output: 21
#
#
#
#
# Example 2:
#
#
# Input: 21
# Output: -1
#


class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        if len(n) == 1:
            return -1
        stack = [n[-1]]
        for i in range(len(n)-2, -1, -1):
            if n[i] >= stack[-1]:
                stack.append(n[i])
            else:
                j = len(stack)-1
                while j >= 1:
                    if n[i] >= stack[j-1]:
                        break
                    j -= 1
                tmp = stack[j]
                stack[j] = n[i]
                res = int(''.join(n[:i]) + tmp + ''.join(sorted(stack)))
                return res if res <= 2**31-1 else -1
        return -1
