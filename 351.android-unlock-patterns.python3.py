#
# [351] Android Unlock Patterns
#
# https://leetcode.com/problems/android-unlock-patterns/description/
#
# algorithms
# Medium (44.59%)
# Total Accepted:    22.1K
# Total Submissions: 49.6K
# Testcase Example:  '1\n1'
#
#
# Given an Android 3x3 key lock screen and two integers m and n, where  1 ≤ m ≤
# n ≤ 9, count the total number of unlock patterns of the Android lock screen,
# which consist of minimum of m keys and maximum n keys.
#
# Rules for a valid pattern:
#
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any
# other keys, the other keys must have previously selected in the pattern. No
# jumps through non selected key is allowed.
# The order of keys used matters.
#
#
#
#
#
# Explanation:
#
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
#
#
#
# Invalid move: 4 - 1 - 3 - 6
#
# Line  1 - 3 passes through key 2 which had not been selected in the pattern.
#
# Invalid move: 4 - 1 - 9 - 2
#
# Line  1 - 9 passes through key 5 which had not been selected in the pattern.
#
# Valid move: 2 - 4 - 1 - 3 - 6
#
# Line 1 - 3 is valid because it passes through key 2, which had been selected
# in the pattern
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
#
# Line 1 - 9 is valid because it passes through key 5, which had been selected
# in the pattern.
#
# Example:
# Given m = 1, n = 1, return 9.
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.dic = {(1, 3): 2, (1, 7): 4, (1, 9): 5,
                    (2, 8): 5,
                    (3, 1): 2, (3, 9): 6, (3, 7): 5,
                    (4, 6): 5,
                    (6, 4): 5,
                    (7, 9): 8, (7, 1): 4, (7, 3): 5,
                    (8, 2): 5,
                    (9, 1): 5, (9, 3): 6, (9, 7): 8}
        visited = [False]*10
        self.res = 0
        for i in range(1, 10):
            visited[i] = True
            self.DFS(i, 1, m, n, visited)
            visited[i] = False
        return self.res

    def DFS(self, x, cur, m, n, visited):
        if cur >= m and cur <= n:
            self.res += 1
        if cur > n:
            return
        for i in range(1, 10):
            if i != x and not visited[i]:
                if (x, i) in self.dic:
                    if visited[self.dic[(x, i)]]:
                        visited[i] = True
                        self.DFS(i, cur+1, m, n, visited)
                        visited[i] = False
                else:
                    visited[i] = True
                    self.DFS(i, cur+1, m, n, visited)
                    visited[i] = False
