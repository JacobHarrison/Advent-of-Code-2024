# -*- coding: utf-8 -*-

# Day 13, Star 2 - Advent of Code 2024

def parse_file():
    sets = []
    with open('input.txt', 'r') as file:
        lines = file.read().strip().split('\n')
        for i in range(0, len(lines), 4):
            set_data = {}
            
            a_values = lines[i].split(': ')[1].split(', ')
            b_values = lines[i+1].split(': ')[1].split(', ')
            prize_values = lines[i+2].split(': ')[1].split(', ')
            
            set_data['Button_A'] = {
                'X': int(a_values[0][2:]),
                'Y': int(a_values[1][2:])
            }
            
            set_data['Button_B'] = {
                'X': int(b_values[0][2:]),
                'Y': int(b_values[1][2:])
            }
            
            set_data['Prize'] = {
                'X': int(prize_values[0][2:]) + 10000000000000,
                'Y': int(prize_values[1][2:]) + 10000000000000
            }
            
            sets.append(set_data)
    
    return sets

parsed_data = parse_file()
total_tokens = 0
for data in parsed_data:
    numerator_a = data['Button_B']['Y'] * data['Prize']['X'] - data['Button_B']['X'] * data['Prize']['Y']
    denominator_a = data['Button_B']['Y'] * data['Button_A']['X'] - data['Button_B']['X'] * data['Button_A']['Y']
    a = numerator_a / denominator_a
    b = (data['Prize']['X'] - data['Button_A']['X'] * a) / data['Button_B']['X']
    if a.is_integer() and b.is_integer():
        total_tokens += (3 * a + b) 

print(int(total_tokens))