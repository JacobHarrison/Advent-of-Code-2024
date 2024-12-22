# -*- coding: utf-8 -*-

# Day 2, Star 1 - Advent of Code 2024

def is_ascending_or_descending(input_list):
    return input_list == sorted(input_list) or input_list == sorted(input_list, reverse=True)

def adjacent_difference_is_at_least_one_and_at_most_three(input_list):
    for i in range(1, len(input_list)):
        difference = abs(input_list[i] - input_list[i - 1])
        if difference < 1 or difference > 3:
            return False
    return True

reports_list = []

with open('input.txt', 'r') as file:
    for line in file:
        reports = list(map(int, line.strip().split()))
        reports_list.append(reports)

safe_count = 0

for reports in reports_list:
    safe = is_ascending_or_descending(reports) and adjacent_difference_is_at_least_one_and_at_most_three(reports)
    if safe:
        safe_count += 1
        
print(safe_count)