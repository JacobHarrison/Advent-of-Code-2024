# -*- coding: utf-8 -*-

# Day 2, Star 2 - Advent of Code 2024

def is_ascending_or_descending(input_list):
    return input_list == sorted(input_list) or input_list == sorted(input_list, reverse=True)

def adjacent_difference_is_at_least_one_and_at_most_three(input_list):
    for i in range(1, len(input_list)):
        difference = abs(input_list[i] - input_list[i - 1])
        if difference < 1 or difference > 3:
            return False
    return True

def can_be_safe_by_removing_one(input_list):
    for i in range(len(input_list)):
        modified_list = input_list[:i] + input_list[i + 1:]
        if is_ascending_or_descending(modified_list) and adjacent_difference_is_at_least_one_and_at_most_three(modified_list):
            return True
    return False

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
    else:
        safe_without_one = can_be_safe_by_removing_one(reports)
        if safe_without_one:
            safe_count += 1
        
print(safe_count)