#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (42.67%)
# Total Accepted:    33.6K
# Total Submissions: 78.7K
# Testcase Example:  '[ ["a","b"],["b","c"] ]\n[2.0,3.0]\n[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]'
#
#
# Equations are given in the format A / B = k, where  A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given  a / b = 2.0, b / c = 3.0. queries are:  a / c = ?,  b / a = ?, a / e =
# ?,  a / a = ?, x / x = ? . return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
#
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
#
#
# According to the example above:
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
#
#
#
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
#
import collections


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = dict()
        # Build Graph
        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, v))
            if v != 0.0:
                graph[b].append((a, 1/v))
        # Queries
        res = []
        for a, b in queries:
            if a in graph and b in graph:
                que, visited, flag = collections.deque(), set(), False
                visited.add(a)
                que.append((a, 1.0))
                while len(que) != 0:
                    cur, v = que.popleft()
                    if cur not in graph[a]:
                        graph[a].append((cur, v))
                        if v != 0.0:
                            graph[cur].append((a, 1/v))
                    if cur == b:
                        res.append(v)
                        flag = True
                        break
                    for nxt in graph[cur]:
                        if nxt[0] not in visited:
                            visited.add(nxt[0])
                            que.append((nxt[0], v*nxt[1]))
                if not flag:
                    res.append(-1.0)
            else:
                res.append(-1.0)
        return res
