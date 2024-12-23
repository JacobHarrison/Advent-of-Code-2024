# -*- coding: utf-8 -*-

# Day 5, Star 1 - Advent of Code 2024

rules = []
updates = []

with open('input.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        if not stripped_line:
            continue
        elif "|" in stripped_line:
            rules.append(tuple(map(int, stripped_line.split("|"))))
        else:
            updates.append(list(map(int, stripped_line.split(","))))        

def check_order(lst, num1, num2):
    if num1 in lst and num2 in lst:
        return lst.index(num1) < lst.index(num2)
    return True

answer = 0

for update in updates:
    is_valid = True
    for first_number, second_number in rules:
        if not check_order(update, first_number, second_number):
            is_valid = False
            break
    if is_valid:
        answer += update[len(update) // 2]
        
print(answer)
