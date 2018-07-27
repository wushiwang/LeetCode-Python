#
# [587] Erect the Fence
#
# https://leetcode.com/problems/erect-the-fence/description/
#
# algorithms
# Hard (33.68%)
# Total Accepted:    5.1K
# Total Submissions: 15.3K
# Testcase Example:  '[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]'
#
# There are some trees, where each tree is represented by (x,y) coordinate in a
# two-dimensional garden. Your job is to fence the entire garden using the
# minimum length of rope as it is expensive. The garden is well fenced only if
# all the trees are enclosed. Your task is to help find the coordinates of
# trees which are exactly located on the fence perimeter.
#
# Example 1:
#
# Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation:
#
#
#
#
# Example 2:
#
# Input: [[1,2],[2,2],[4,2]]
# Output: [[1,2],[2,2],[4,2]]
# Explanation:
#
# Even you only have trees in a line, you need to use rope to enclose them.
#
#
#
# ⁠Note:
#
# All trees should be enclosed together. You cannot cut the rope to enclose
# trees that will separate them in more than one group.
# All input integers will range from 0 to 100.
# The garden has at least one tree.
# All coordinates are distinct.
# Input points have NO order. No order required for output.
#
# Solution from:
# https://leetcode.com/problems/erect-the-fence/discuss/103300/Detailed-explanation-of-Graham-scan-in-14-lines-(Python)


class Solution:
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        def cross(p1, p2, p3):
            return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)

        # Computes slope of line between p1 and p2
        def slope(p1, p2):
            return 1.0*(p1.y-p2.y)/(p1.x-p2.x) if p1.x != p2.x else float('inf')

        # Find the smallest left point and remove it from
        # points
        start = min(points, key=lambda p: (p.x, p.y))
        points.pop(points.index(start))

        # Sort points so that traversal is from start
        # in a ccw circle.
        points.sort(key=lambda p: (slope(p, start), -p.y, p.x))

        # Add each point to the convex hull.
        # If the last 3 points make a cw turn,
        # the second to last point is wrong.
        ans = [start]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(ans[-3], ans[-2], ans[-1]) < 0:
                ans.pop(-2)

        return ans
