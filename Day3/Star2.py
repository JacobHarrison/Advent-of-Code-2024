# -*- coding: utf-8 -*-

# Day 3, Star 2 - Advent of Code 2024
import re

def get_numbers(match):
    numbers = re.findall(r"\d{1,3}", match)
    return int(numbers[0]), int(numbers[1])

with open('input.txt', 'r') as file:
    content = file.read()

regex_pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

matches = re.findall(regex_pattern, content)
is_enabled = True
answer = 0

for match in matches:
    if match == "do()":
        is_enabled = True
    elif match == "don't()":
        is_enabled = False
    elif is_enabled:
        a, b = get_numbers(match)
        answer += a * b

print(answer)