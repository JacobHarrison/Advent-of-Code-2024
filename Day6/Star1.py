# -*- coding: utf-8 -*-

# Day 6, Star 1 - Advent of Code 2024

def count_positions(current_maze):
    return sum(position.count("X") for position in current_maze)

def can_escape(current_guard_pos, current_move, current_maze):
    new_row = current_guard_pos[0] + current_move[0]
    new_column = current_guard_pos[1] + current_move[1]    
    if not (0 <= new_row < len(current_maze) and 0 <= new_column < len(current_maze[0])):
        return True
    return False

def can_move(current_guard_pos, current_move, current_maze):
    new_row = current_guard_pos[0] + current_move[0]
    new_column = current_guard_pos[1] + current_move[1]
    if current_maze[new_row][new_column] == "#":
        return False
    return True

def make_move(current_guard_pos, current_move, current_maze):
    new_row = current_guard_pos[0] + current_move[0]
    new_column = current_guard_pos[1] + current_move[1]
    current_maze[new_row][new_column] = "X"
    return (new_row, new_column)


def turn(current_move):
    move_up = (-1,0)
    move_down = (1,0)
    move_right = (0,1)
    move_left = (0,-1)
    if current_move == move_up:
        return move_right
    elif current_move == move_right:
        return move_down
    elif current_move == move_down:
        return move_left
    else:
        return move_up

def open_file():
    index = 0
    maze = []
    guard_pos = (0,0)
    with open('input.txt', 'r') as file:
        for line in file:
            stripped_line = list(line.strip())
            maze.append(stripped_line)
            if "^" in stripped_line:
                guard_pos = (index, stripped_line.index("^"))
            index += 1
        return maze, guard_pos

def play_game(maze, guard_pos):
    move = (-1,0)
    guard_active = True
    current_maze = maze
    current_guard_pos = guard_pos
    while guard_active:
        if can_escape(current_guard_pos, move, current_maze):
            guard_active = False
        elif can_move(current_guard_pos, move, current_maze):
            current_guard_pos = make_move(current_guard_pos, move, current_maze)
        else:
            move = turn(move)
    return count_positions(current_maze)

maze, guard_pos = open_file()
answer = play_game(maze, guard_pos)
print(answer)
