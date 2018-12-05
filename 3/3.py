import re

# Getting input data
with open('./input.txt') as file:
    inputs = file.readlines()

"""
part 1
"""
pattern = '\#(\d+)(\s\@\s)(\d+),(\d+):\s(\d+)x(\d+)'

#init grid
matrix = [[0 for x in range(1000)] for y in range(1000)]
overlapping = 0

for line in inputs:
    check = re.search(pattern, line.strip())
    _id, _x, _y, _w, _h = int(check.group(1)), int(check.group(3)), int(check.group(4)), int(check.group(5)), int(check.group(6))
    
    for i in range(_x, _x+_w):        
        for j in range(_y, _y+_h):
            # since it starts at 0, I can skip the check and just add 1 each time I encounter it
            matrix[j][i] += 1

for col in matrix:
    for cell in col:
        if cell > 1:
            overlapping += 1

print(overlapping)

"""
part 2
"""

"""
Actually, I can reuse the previouse snippet
matrix = [[0 for x in range(1000)] for y in range(1000)]

# populate the matrix with fabrics' ids
for line in inputs:
    check = re.search(pattern, line.strip())
    _id, _x, _y, _w, _h = int(check.group(1)), int(check.group(3)), int(check.group(4)), int(check.group(5)), int(check.group(6))
        
    for i in range(_x, _x+_w):
        for j in range(_y, _y+_h):
            matrix[j][i] += 1
"""

# recheck and pick only those cell whose _id is placed as per specs
the_only_one = 0
for line in inputs:
    check = re.search(pattern, line.strip())
    _id, _x, _y, _w, _h = int(check.group(1)), int(check.group(3)), int(check.group(4)), int(check.group(5)), int(check.group(6))
        
    taken = False
    # if even one of the cell is different from 1 means it's either empty (0) or overlapping.
    # if ALL the cell of this piece of fabric equals to 1 then we have a match
    for i in range(_x, _x+_w):
        for j in range(_y, _y+_h):
            if matrix[j][i] != 1:
                taken = True

    if not taken:
        the_only_one = _id

print(the_only_one)