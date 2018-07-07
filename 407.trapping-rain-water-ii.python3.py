#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (37.75%)
# Total Accepted:    18.4K
# Total Submissions: 48.9K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n matrix of positive integers representing the height of each
# unit cell in a 2D elevation map, compute the volume of water it is able to
# trap after raining.
#
#
# Note:
# Both m and n are less than 110. The height of each unit cell is greater than
# 0 and is less than 20,000.
#
#
# Example:
#
# Given the following 3x6 height map:
# [
# ⁠ [1,4,3,1,3,2],
# ⁠ [3,2,1,3,2,4],
# ⁠ [2,3,3,2,3,1]
# ]
#
# Return 4.
#
#
#
#
#
# The above image represents the elevation map
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
#
#
#
#
# After the rain, water is trapped between the blocks. The total volume of
# water trapped is 4.
#
import heapq


class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # BFS + Priority Queue
        heap, visited = [], [[False for x in range(len(heightMap[0]))] for y in range(len(heightMap))]
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i == 0 or j == 0 or i == len(heightMap)-1 or j == len(heightMap[0])-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        res = 0
        while len(heap) != 0:
            cur, x, y = heapq.heappop(heap)
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if nx >= 0 and nx < len(heightMap) and ny >= 0 and ny < len(heightMap[0]):
                    if not visited[nx][ny]:
                        if heightMap[nx][ny] < cur:
                            res += cur - heightMap[nx][ny]
                            heapq.heappush(heap, (cur, nx, ny))
                            visited[nx][ny] = True
                        else:
                            heapq.heappush(heap, (heightMap[nx][ny], nx, ny))
                            visited[nx][ny] = True
        return res
