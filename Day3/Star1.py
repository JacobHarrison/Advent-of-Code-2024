# -*- coding: utf-8 -*-

# Day 3, Star 1 - Advent of Code 2024
import re

with open('input.txt', 'r') as file:
    content = file.read()

regex_pattern = r'mul\((\d+),\s*(\d+)\)'

matches = re.findall(regex_pattern, content)

answer = sum(int(num1) * int(num2) for num1, num2 in matches)

print(answer)