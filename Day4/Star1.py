# -*- coding: utf-8 -*-

# Day 4, Star 1 - Advent of Code 2024

word_maze = []
with open('input.txt', 'r') as file:
    for line in file:
        word_maze.append(line.strip())
        
def search_direction(row, column, delta_r, delta_c):
        word_len = len("XMAS")
        for i in range(word_len):
            new_row, new_column = row + i * delta_r, column + i * delta_c
            if new_row < 0 or new_row >= len(word_maze) or new_column < 0 or new_column >= len(word_maze[0]):
                return False
            if word_maze[new_row][new_column] != "XMAS"[i]:
                return False
        return True

answer = 0

for row in range(len(word_maze)):
    for column in range(len(word_maze[row])):
        for delta_r, delta_c in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if search_direction(row, column, delta_r, delta_c):
                answer += 1

print(answer)