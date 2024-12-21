# -*- coding: utf-8 -*-

# Day 1, Star 2 - Advent of Code 2024

first_list_location_ids = []
second_list_location_ids = []

second_list_frequency_map = {}

with open('input.txt','r') as file:
    for line in file:
        part1, part2 = map(int, line.strip().split(' ', 1))
        first_list_location_ids.append(part1)
        second_list_location_ids.append(part2)
        if part2 in second_list_frequency_map:
            second_list_frequency_map[part2] += 1
        else:
            second_list_frequency_map[part2] = 1

answer = 0

for location_id in first_list_location_ids:
    if location_id in second_list_frequency_map:
        answer += location_id * second_list_frequency_map[location_id]

print(answer)