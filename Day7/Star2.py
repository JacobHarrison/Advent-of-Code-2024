# -*- coding: utf-8 -*-

# Day 7, Star 2 - Advent of Code 2024

def check_combos(target, numbers):
    def backtrack(index, current_value):
        if index == len(numbers):
            return current_value == target

        if backtrack(index + 1, current_value + numbers[index]):
            return True

        if backtrack(index + 1, current_value * numbers[index]):
            return True
        
        concat_value = int(str(current_value) + str(numbers[index]))
        if backtrack(index + 1, concat_value):
            return True
        
        return False

    return backtrack(1, numbers[0])


answer = 0
with open('test.txt', 'r') as file:
    lines = file.readlines()


for line in lines:
    test_value, number_list = line.strip().split(':')
    target = int(test_value)
    numbers = list(map(int, number_list.split()))
    answer += target if check_combos(target, numbers) else 0

print(answer)