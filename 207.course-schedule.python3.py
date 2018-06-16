#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (34.09%)
# Total Accepted:    129.9K
# Total Submissions: 380.7K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
#
# Example 1:
#
#
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
#
#
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
#
#
# Note:
#
#
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
#


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Toplogical sort
        graph, ind = [[] for x in range(numCourses)], [0 for x in range(numCourses)]
        for e in prerequisites:
            graph[e[0]].append(e[1])
            ind[e[1]] += 1
        zeroInd, clear = set(), 0
        for v in range(numCourses):
            if ind[v] == 0:
                zeroInd.add(v)
        while len(zeroInd) != 0:
            s = zeroInd.pop()
            for v in graph[s]:
                ind[v] -= 1
                if ind[v] == 0:
                    zeroInd.add(v)
            graph[s].clear()
            clear += 1
        if clear != numCourses:
            # Has cycle
            return False
        return True
