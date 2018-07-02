#
# [353] Design Snake Game
#
# https://leetcode.com/problems/design-snake-game/description/
#
# algorithms
# Medium (27.47%)
# Total Accepted:    12.3K
# Total Submissions: 44.9K
# Testcase Example:  '["SnakeGame","move","move","move","move","move","move"]\n[[3,2,[[1,2],[0,1]]],["R"],["D"],["R"],["U"],["L"],["U"]]'
#
# Design a Snake game that is played on a device with screen size = width x
# height. Play the game online if you are not familiar with the game.
#
# The snake is initially positioned at the top left corner (0,0) with length =
# 1 unit.
#
# You are given a list of food's positions in row-column order. When a snake
# eats the food, its length and the game's score both increase by 1.
#
# Each food appears one by one on the screen. For example, the second food will
# not appear until the first food was eaten by the snake.
#
# When a food does appear on the screen, it is guaranteed that it will not
# appear on a block occupied by the snake.
#
#
# Example:
#
# Given width = 3, height = 2, and food = [[1,2],[0,1]].
#
# Snake snake = new Snake(width, height, food);
#
# Initially the snake appears at position (0,0) and the food at (1,2).
#
# |S| | |
# | | |F|
#
# snake.move("R"); -> Returns 0
#
# | |S| |
# | | |F|
#
# snake.move("D"); -> Returns 0
#
# | | | |
# | |S|F|
#
# snake.move("R"); -> Returns 1 (Snake eats the first food and right after
# that, the second food appears at (0,1) )
#
# | |F| |
# | |S|S|
#
# snake.move("U"); -> Returns 1
#
# | |F|S|
# | | |S|
#
# snake.move("L"); -> Returns 2 (Snake eats the second food)
#
# | |S|S|
# | | |S|
#
# snake.move("U"); -> Returns -1 (Game over because snake collides with
# border)
#
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
import collections


class SnakeGame:

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.food = food
        self.food_p = 0
        if self.food_p < len(self.food):
            self.food_pos = tuple(self.food[0])
            self.food_p += 1
        else:
            self.food_p = -1
        self.snake = collections.deque([(0, 0)])
        self.snake_set = {(0, 0)}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        d = {'U': 2, 'L': 3, 'R': 0, 'D': 1}
        x, y = self.snake[-1]
        nx, ny = x+dx[d[direction]], y+dy[d[direction]]
        if nx >= 0 and nx < self.height and ny >= 0 and ny < self.width:
            if (nx, ny) in self.snake_set:
                if (nx, ny) == self.snake[0]:
                    self.snake.popleft()
                    self.snake.append((nx, ny))
                else:
                    return -1
            elif self.food_p != -1 and (nx, ny) == self.food_pos:
                self.snake.append((nx, ny))
                self.snake_set.add((nx, ny))
                if self.food_p < len(self.food):
                    self.food_pos = tuple(self.food[self.food_p])
                    self.food_p += 1
                else:
                    self.food_p = -1
            else:
                self.snake.append((nx, ny))
                self.snake_set.add((nx, ny))
                tail = self.snake.popleft()
                self.snake_set.remove(tail)
            return len(self.snake)-1
        else:
            return -1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
