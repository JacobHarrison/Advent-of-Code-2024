# -*- coding: utf-8 -*-

# Day 11, Star 2 - Advent of Code 2024
from functools import lru_cache

with open("input.txt", "r") as file:
    data = list(map(int, file.readline().strip().split()))

@lru_cache(maxsize=None)
def count_stones(stone, blinks_left):
    if blinks_left == 0:
        return 1
    
    if stone == 0:
        return count_stones(1, blinks_left - 1)
    
    stone_str = str(stone)
    length = len(stone_str)
    
    if length % 2 == 0:
        half = length // 2
        return count_stones(int(stone_str[:half]), blinks_left - 1) + count_stones(int(stone_str[half:]), blinks_left - 1)
    else:
        return count_stones(stone * 2024, blinks_left - 1)

answer = 0
for stone in data:
    answer += count_stones(stone, 75)

print(answer)