# -*- coding: utf-8 -*-

# Day 12, Star 1 - Advent of Code 2024
from collections import defaultdict

garden = []
visited = set()
group_id = 0
group_log = defaultdict(set)
neighbor_log = defaultdict(int)
neighbor_to_perimeter = {4: 0, 3: 1, 2: 2, 1: 3, 0: 4}
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

with open("input.txt", "r") as file:
    for line in file:
        garden.append(list(line.strip()))

def check_neighbors(row, col, visited, group_id):
    if (row, col) in visited:
        return
    
    plant_type = garden[row][col]
    if not group_log[plant_type + str(group_id)]:
        group_log[plant_type + str(group_id)].add((row, col))
        
    visited.add((row, col))
    neighbors = 0
    for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(garden) and 0 <= nc < len(garden[0]):
                if plant_type == garden[nr][nc]:
                    neighbors += 1
                    if (nr, nc) not in group_log[plant_type + str(group_id)]:
                        group_log[plant_type + str(group_id)].add((nr, nc))
                        check_neighbors(nr, nc, visited, group_id)
    neighbor_log[(row, col)] = neighbors
                    
                    
for row_index, row in enumerate(garden):
    for col_index, plant in enumerate(row):
        check_neighbors(row_index, col_index, visited, group_id)
        group_id += 1

total_price = 0
for group in group_log:
    perimeter = 0
    area = len(group_log[group])
    for coords in group_log[group]:
        perimeter += neighbor_to_perimeter.get(neighbor_log[coords])
    price = perimeter * area
    total_price += price
    
print(total_price)