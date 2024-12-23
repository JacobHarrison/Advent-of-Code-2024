# -*- coding: utf-8 -*-

# Day 5, Star 2 - Advent of Code 2024

rules = []
updates = []
left_before_right = {}

with open('input.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        if not stripped_line:
            continue
        elif "|" in stripped_line:
            left_right = tuple(map(int, stripped_line.split("|")))
            if left_right in left_before_right:
                left_before_right[left_right[0]].append(left_right[1])
            else:
                left_before_right[left_right[0]] = [left_right[1]]
            rules.append(left_right)
        else:
            updates.append(list(map(int, stripped_line.split(","))))        

def check_order(lst, num1, num2):
    if num1 in lst and num2 in lst:
        return lst.index(num1) < lst.index(num2)
    return True

def fix_complete(update):
    for first, second in rules:
        if not check_order(update, first, second):
            return False
    return True

answer = 0

for update in updates:
    is_valid = True
    for first_number, second_number in rules:
        if not check_order(update, first_number, second_number):
            is_valid = False
            break
    if not is_valid:
        index = 0
        while index < len(rules):
            left_rule, right_rule = rules[index]
            if left_rule not in update or right_rule not in update:
                index += 1
                continue
            left = update.index(left_rule)
            right = update.index(right_rule)
            if left < right:
                index += 1
                continue
            temp = update[left]
            update[left] = update[right]
            update[right] = temp
            index = 0
        answer += update[len(update) // 2]

print(answer)