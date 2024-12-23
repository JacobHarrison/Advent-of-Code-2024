# -*- coding: utf-8 -*-

# Day 6, Star 2 - Advent of Code 2024

def can_escape(current_guard_pos, current_move, current_maze):
    new_row = current_guard_pos[0] + current_move[0]
    new_column = current_guard_pos[1] + current_move[1]    
    if not (0 <= new_row < len(current_maze) and 0 <= new_column < len(current_maze[0])):
        return True
    return False

def can_move(current_guard_pos, current_move, current_maze):
    new_row = current_guard_pos[0] + current_move[0]
    new_column = current_guard_pos[1] + current_move[1]
    if current_maze[new_row][new_column] == "#" or current_maze[new_row][new_column] == "O":
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

def is_loop(maze, guard_pos):
    move = (-1,0)
    current_maze = maze
    current_guard_pos = guard_pos
    previous_moves = set()
    while True:
        if can_escape(current_guard_pos, move, current_maze):
            return False
        elif can_move(current_guard_pos, move, current_maze):
            if (current_guard_pos, move) in previous_moves:
                return True
            previous_moves.add((current_guard_pos, move))
            current_guard_pos = make_move(current_guard_pos, move, current_maze)
        else:
            move = turn(move)

def try_blocker_positions(maze, guard_pos):
    answer = 0
    for row_index, row in enumerate(maze):
        for col_index, column in enumerate(row):
            if column == "#" or column == "^":
                continue
            test_maze = maze[:]
            row_list = list(test_maze[row_index])
            row_list[col_index] = "#"
            test_maze[row_index] = row_list
            test_guard = tuple(guard_pos)
            if is_loop(test_maze, test_guard):
                answer += 1            

maze, guard_pos = open_file()
answer = try_blocker_positions(maze, guard_pos)
print(answer)