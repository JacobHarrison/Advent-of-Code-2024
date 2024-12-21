# -*- coding: utf-8 -*-

# Day 1, Star 1 - Advent of Code 2024

first_list_location_ids = []
second_list_location_ids = []

with open('input.txt','r') as file:
    for line in file:
        part1, part2 = map(int, line.strip().split(' ', 1))
        first_list_location_ids.append(part1)
        second_list_location_ids.append(part2)
        
first_list_location_ids.sort()
second_list_location_ids.sort()

differences = [abs(a - b) for a, b in zip(first_list_location_ids, second_list_location_ids)]

total = sum(differences)

print(total)