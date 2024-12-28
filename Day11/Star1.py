# -*- coding: utf-8 -*-

# Day 11, Star 1 - Advent of Code 2024
with open("input.txt", "r") as file:
    data = list(map(int, file.readline().strip().split()))
    
def expand_stones(stones, iteration):
    if iteration == 25:
        return len(stones)
    
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left = int(str(stone)[:half])
            right = int(str(stone)[half:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(stone * 2024)
            
    return expand_stones(new_stones, iteration + 1)  
    
answer = expand_stones(data, 0)
print(answer)