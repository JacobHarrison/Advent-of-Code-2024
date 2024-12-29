# -*- coding: utf-8 -*-

# Day 12, Star 2 - Advent of Code 2024
from collections import defaultdict

garden = []
visited = set()
group_id = 0
group_log = defaultdict(set)
neighbor_log = defaultdict(int)
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

def check_north(r, c, sorted_coords, n, w, nw):
    if n not in sorted_coords:
        same_edge = (w in sorted_coords) and (nw not in sorted_coords)
        if not same_edge:
            return 1
    return 0

def check_south(r, c, sorted_coords, w, s, sw):
    if s not in sorted_coords:
      same_edge = (w in sorted_coords) and (sw not in sorted_coords)
      if not same_edge:
        return 1
    return 0

def check_west(r, c, sorted_coords, n, w, nw):
    if w not in sorted_coords:
      same_edge = (n in sorted_coords) and (nw not in sorted_coords)
      if not same_edge:
        return 1
    return 0

def check_east(r, c, sorted_coords, e, n, ne):
    if e not in sorted_coords:
      same_edge = (n in sorted_coords) and (ne not in sorted_coords)
      if not same_edge:
        return 1
    return 0

total_price = 0
for group in group_log:
    area = len(group_log[group])
    group_coords = group_log[group]
    sides = 0
    for (r, c) in group_coords:
        n = (r - 1, c)
        w = (r, c - 1)
        nw = (r - 1, c - 1)
        s = (r + 1, c)
        sw = (r + 1, c - 1)
        e = (r, c + 1)
        ne = (r - 1, c + 1)
        sides += check_north(r, c, group_coords, n, w, nw)
        sides += check_south(r, c, group_coords, w, s, sw)
        sides += check_west(r, c, group_coords, n, w, nw)
        sides += check_east(r, c, group_coords, e, n, ne)
    price = area * sides
    total_price += price
    
print(total_price)
