# -*- coding: utf-8 -*-

# Day 10, Star 2 - Advent of Code 2024
with open("input.txt", "r") as file:
    topo_map = [list(map(int, line.strip())) for line in file]

def dfs(height_map, x, y):
    stack = [(x, y, 0)]
    distinct_paths = 0
    
    while stack:
        cx, cy, current_height = stack.pop()
        
        if height_map[cx][cy] == 9:
            distinct_paths += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = cx + dx, cy + dy
            if 0 <= new_x < len(height_map) and 0 <= new_y < len(height_map[0]) and (new_x, new_y) and height_map[new_x][new_y] == current_height + 1:
                new_height = height_map[new_x][new_y]
                stack.append((new_x, new_y, new_height))
    
    return distinct_paths

answer = 0
    
for row_index, row in enumerate(topo_map):
    for col_index, altitude in enumerate(row):
        if altitude == 0:
            answer += dfs(topo_map, row_index, col_index)

print(answer)