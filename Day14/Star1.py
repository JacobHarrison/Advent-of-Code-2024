# -*- coding: utf-8 -*-

# Day 14, Star 1 - Advent of Code 2024
from functools import reduce
width = 101
height = 103

class Robot:
    def __init__(self, p, v):
        self.p = p
        self.v = v
    
    def move(self):
        new_x = (self.p[0] + self.v[0]) % width
        new_y = (self.p[1] + self.v[1]) % height
        self.p = (new_x, new_y)
    
    def __repr__(self):
        return f"Robot(p={self.p}, v={self.v})"

def parse_robots():
    robots = []
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        
        for line in lines:
            parts = line.split(' ')
            p_values = tuple(map(int, parts[0].split('=')[1].split(',')))
            v_values = tuple(map(int, parts[1].split('=')[1].split(',')))
            
            robot = Robot(p=p_values, v=v_values)
            robots.append(robot)
    
    return robots

def count_robots_in_quadrants(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    mid_row = rows // 2
    mid_col = cols // 2
    
    top_left = [row[:mid_col] for row in grid[:mid_row]]
    top_right = [row[mid_col+1:] for row in grid[:mid_row]]
    bottom_left = [row[:mid_col] for row in grid[mid_row+1:]]
    bottom_right = [row[mid_col+1:] for row in grid[mid_row+1:]]
    
    top_left_robots = sum(robots for row in top_left for robots in row if isinstance(robots, (int)))
    top_right_robots = sum(robots for row in top_right for robots in row if isinstance(robots, (int)))
    bottom_left_robots = sum(robots for row in bottom_left for robots in row if isinstance(robots, (int)))
    bottom_right_robots = sum(robots for row in bottom_right for robots in row if isinstance(robots, (int)))
    
    return top_left_robots, top_right_robots, bottom_left_robots, bottom_right_robots

robot_list = parse_robots()
robot_map = [['.' for _ in range(width)] for _ in range(height)]
second = 0
while second < 100:
    for robot in robot_list:
        robot.move()
    second += 1

for robot in robot_list:
        x, y = robot.p
        if robot_map[y][x] == '.':
            robot_map[y][x] = 1
        else:
            robot_map[y][x] += 1

print(reduce(lambda x, y: x * y, count_robots_in_quadrants(robot_map)))