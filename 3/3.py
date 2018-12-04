import re

# Getting input data
with open('./input.txt') as file:
    inputs = file.readlines()

"""
part 1
"""
pattern = '\#(\d+)(\s\@\s)(\d+),(\d+):\s(\d+)x(\d+)'

length = 0
height = 0

matrix = [[0 for x in range(1000)] for y in range(1000)]
overlapping = 0

for line in inputs:
    check = re.search(pattern, line.strip())
    _id, _x, _y, _w, _h = int(check.group(1)), int(check.group(3)), int(check.group(4)), int(check.group(5)), int(check.group(6))
    
    for i in range(_x, _x+_w):        
        for j in range(_y, _y+_h):
            if matrix[j][i] == 0:
                matrix[j][i] = 1
            else:
                # increment
                matrix[j][i] += 1
                

for col in matrix:
    for row in col:
        if row > 1:
            overlapping += 1

print(overlapping)