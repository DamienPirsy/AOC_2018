# Getting input data
with open('./input.txt') as file:
    inputs = file.readlines()


"""
part 1
"""
print(sum(map(int, inputs)))

"""
part 2
"""
total = 0    
twice = []
found = False
while not found:
    for line in inputs:
        total += int(line)
        if total in twice:
            print("{} twice".format(total))
            found = True
            break
        else:
            twice.append(total)
                