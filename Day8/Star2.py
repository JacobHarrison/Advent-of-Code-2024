# -*- coding: utf-8 -*-

# Day 8, Star 2 - Advent of Code 2024
from collections import defaultdict

def open_file():
    with open('input.txt', 'r') as file:
        return [list(line.strip()) for line in file]
    
data = open_file()

row_count, col_count = len(data), len(data[0])
antennas = defaultdict(list)

for row in range(row_count):
    for col in range(col_count):
        if data[row][col] != ".":
            antennas[data[row][col]].append((row, col))
            
antinodes = set()
  
for antenna, coords in antennas.items():
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = tuple(a - b for a, b in zip(coords[j], coords[i]))
            for index, direction in [(i, -1), (j, 1)]:
                pos = coords[index]
                while 0 <= pos[0] < row_count and 0 <= pos[1] < col_count:
                    antinodes.add(pos)
                    pos = tuple([a + b * direction for a, b in zip(pos, distance)])
                    
print(len(antinodes))