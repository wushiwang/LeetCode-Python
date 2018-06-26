#
# [302] Smallest Rectangle Enclosing Black Pixels
#
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/
#
# algorithms
# Hard (46.95%)
# Total Accepted:    18.1K
# Total Submissions: 38.5K
# Testcase Example:  '[["0","0","1","0"],
#                      ["0","1","1","0"],
#                      ["0","1","0","0"]]\n0\n2'
#
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a
# black pixel. The black pixels are connected, i.e., there is only one black
# region. Pixels are connected horizontally and vertically. Given the location
# (x, y) of one of the black pixels, return the area of the smallest
# (axis-aligned) rectangle that encloses all black pixels.
#
# Example:
#
#
# Input:
# [
# ⁠ "0010",
# ⁠ "0110",
# ⁠ "0100"
# ]
# and x = 0, y = 2
#
# Output: 6
#


class Solution:
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # Binary Search
        xmin = self.binarySearch(-1, y, image, '1', True)
        xmax = self.binarySearch(y, len(image[0]), image, '0', True)
        ymin = self.binarySearch(-1, x, image, '1', False)
        ymax = self.binarySearch(x, len(image), image, '0', False)

        return int(abs(xmin-xmax))*int(abs(ymin-ymax))

    def binarySearch(self, L, R, image, target, flag):
        # (]
        while L < R-1:
            M = (L + R) >> 1
            if self.check(image, M, flag, target):
                R = M
            else:
                L = M
        return R

    def check(self, image, i, flag, target):
        if flag:
            if target == '1':
                for x in range(len(image)):
                    if image[x][i] == target:
                        return True
                return False
            else:
                for x in range(len(image)):
                    if image[x][i] != target:
                        return False
                return True
        else:
            if target == '1':
                return target in image[i]
            else:
                return '1' not in image[i]
