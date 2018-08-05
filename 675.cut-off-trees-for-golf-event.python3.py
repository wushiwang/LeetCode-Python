#
# [675] Cut Off Trees for Golf Event
#
# https://leetcode.com/problems/cut-off-trees-for-golf-event/description/
#
# algorithms
# Hard (27.27%)
# Total Accepted:    7.5K
# Total Submissions: 27.7K
# Testcase Example:  '[[1,2,3],[0,0,4],[7,6,5]]'
#
#
# You are asked to cut off trees in a forest for a golf event. The forest is
# represented as a non-negative 2D map, in this map:
#
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through,
# and this positive number represents the tree's height.
#
#
#
#
# You are asked to cut off all the trees in this forest in the order of tree's
# height - always cut off the tree with lowest height first. And after cutting,
# the original place has the tree will become a grass (value 1).
#
#
#
# You will start from the point (0, 0) and you should output the minimum steps
# you need to walk to cut off all the trees. If you can't cut off all the
# trees, output -1 in that situation.
#
#
#
# You are guaranteed that no two trees have the same height and there is at
# least one tree needs to be cut off.
#
#
# Example 1:
#
# Input:
# [
# ⁠[1,2,3],
# ⁠[0,0,4],
# ⁠[7,6,5]
# ]
# Output: 6
#
#
#
# Example 2:
#
# Input:
# [
# ⁠[1,2,3],
# ⁠[0,0,0],
# ⁠[7,6,5]
# ]
# Output: -1
#
#
#
# Example 3:
#
# Input:
# [
# ⁠[2,3,4],
# ⁠[0,0,5],
# ⁠[8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in
# (0,0) directly without walking.
#
#
#
#
# Hint: size of the given matrix will not exceed 50x50.
#
import collections


class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if len(forest) == 0:
            return -1
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        height = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    height.append(forest[i][j])
        height, pos = sorted(height), 0
        que, visited, res = collections.deque(), set(), 0
        visited.add((0, 0))
        que.append((0, 0, 0))
        while len(que) != 0 and pos != len(height):
            x, y, l = que.popleft()
            if forest[x][y] == height[pos]:
                res += l
                pos += 1
                que.clear()
                que.append((x, y, 0))
                visited.clear()
                visited.add((x, y))
            else:
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if nx >= 0 and nx < len(forest) and ny >= 0 and ny < len(forest[0]):
                        if (nx, ny) not in visited and forest[nx][ny] != 0:
                            que.append((nx, ny, l+1))
                            visited.add((nx, ny))
        if pos != len(height):
            return -1
        return res
