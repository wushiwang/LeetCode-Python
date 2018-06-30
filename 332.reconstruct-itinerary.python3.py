#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (30.05%)
# Total Accepted:    51.1K
# Total Submissions: 170.2K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
#
# Note:
#
#
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
#
#
# Example 1:
#
#
# Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR",
# "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#
#
# Example 2:
#
#
# Input: tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
#
#
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test
# cases.
#


class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # Construct Graph
        self.graph = dict()
        for a, b in tickets:
            if a not in self.graph:
                self.graph[a] = []
            if b not in self.graph:
                self.graph[b] = []
            self.graph[a].append(b)
        for k in self.graph:
            self.graph[k].sort()
        return self.DFS("JFK", ["JFK"], len(tickets))

    def DFS(self, node, cur, n):
        if len(cur) == n+1:
            return cur
        for i in range(len(self.graph[node])):
            des = self.graph[node][i]
            if des != '':
                self.graph[node][i] = ''
                res = self.DFS(des, cur+[des], n)
                if res is not None:
                    return res
                self.graph[node][i] = des
        return
