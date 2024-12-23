# -*- coding: utf-8 -*-

# Day 4, Star 2 - Advent of Code 2024

word_maze = []
with open('input.txt', 'r') as file:
    for line in file:
        word_maze.append(line.strip())

def search_X_pattern(row, column):
    if word_maze[row][column] != "A":
        return False
    
    top_right_row, top_right_column = row + 1, column + 1
    top_left_row, top_left_column = row + 1, column - 1
    bottom_right_row, bottom_right_column = row - 1, column + 1
    bottom_left_row, bottom_left_column = row - 1, column - 1
    
    if not (0 <= top_right_row < len(word_maze) and 0 <= top_right_column < len(word_maze[row])):
        return False
    if not (0 <= top_left_row < len(word_maze) and 0 <= top_left_column < len(word_maze[row])):
        return False
    if not (0 <= bottom_right_row < len(word_maze) and 0 <= bottom_right_column < len(word_maze[row])):
        return False
    if not (0 <= bottom_left_row < len(word_maze) and 0 <= bottom_left_column < len(word_maze[row])):
        return False
    
    top_right_S = word_maze[top_right_row][top_right_column] == "S"
    top_right_M = word_maze[top_right_row][top_right_column] == "M"
    top_left_S = word_maze[top_left_row][top_left_column] == "S"
    top_left_M = word_maze[top_left_row][top_left_column] == "M"
    bottom_right_S = word_maze[bottom_right_row][bottom_right_column] == "S"
    bottom_right_M = word_maze[bottom_right_row][bottom_right_column] == "M"
    bottom_left_S = word_maze[bottom_left_row][bottom_left_column] == "S"
    bottom_left_M = word_maze[bottom_left_row][bottom_left_column] == "M"
    
    left_right_diagonal = (top_right_S and bottom_left_M) or (top_right_M and bottom_left_S)
    right_left_diagonal = (top_left_S and bottom_right_M) or (top_left_M and bottom_right_S)
    
    if left_right_diagonal and right_left_diagonal:
        return True
    return False
        
answer = 0

for row in range(len(word_maze)):
    for column in range(len(word_maze[row])):
        if search_X_pattern(row, column):
            answer += 1

print(answer)