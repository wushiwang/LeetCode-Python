#
# [531] Lonely Pixel I
#
# https://leetcode.com/problems/lonely-pixel-i/description/
#
# algorithms
# Medium (56.47%)
# Total Accepted:    12.4K
# Total Submissions: 22K
# Testcase Example:  '[["W","W","B"],["W","B","W"],["B","W","W"]]'
#
# Given a picture consisting of black and white pixels, find the number of
# black lonely pixels.
#
# The picture is represented by a 2D char array consisting of 'B' and 'W',
# which means black and white pixels respectively.
#
# A black lonely pixel is character 'B' that located at a specific position
# where the same row and same column don't have any other black pixels.
#
# Example:
#
# Input:
# [['W', 'W', 'B'],
# ⁠['W', 'B', 'W'],
# ⁠['B', 'W', 'W']]
#
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
#
#
#
# Note:
#
# The range of width and height of the input 2D array is [1,500].
#


class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        row = [False]*(len(picture))
        col = [False]*(len(picture[0]))
        for i in range(len(picture)):
            cur, flag = 0, True
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    cur += 1
                if cur == 2:
                    flag = False
                    break
            row[i] = flag
        for j in range(len(picture[0])):
            cur, flag = 0, True
            for i in range(len(picture)):
                if picture[i][j] == 'B':
                    cur += 1
                if cur == 2:
                    flag = False
                    break
            col[j] = flag
        res = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and row[i] and col[j]:
                    res += 1
        return res
