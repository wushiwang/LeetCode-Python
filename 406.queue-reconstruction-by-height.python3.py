#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (56.70%)
# Total Accepted:    49.9K
# Total Submissions: 88K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
#
#
# Note:
# The number of people is less than 1,100.
#
#
#
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: x[1])
        res = []
        for p in people:
            cur, i = 0, 0
            while i < len(res):
                if res[i][0] >= p[0]:
                    cur += 1
                    if cur == p[1] + 1:
                        break
                i += 1
            res.insert(i, p)
        return res
