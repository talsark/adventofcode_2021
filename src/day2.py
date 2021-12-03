"""Day 2: Dive!
forward: add to horizontal position
down: add to depth
up: subtract from depth
dive: total horizontal position multiplied by total depth
"""

f = open("C:/Users/talee/Documents/GitHub/adventofcode_2021/inputs/day2.txt", "r")
commands = [line.split() for line in f]


horizontal_position = 0
depth = 0
for command in commands:
    if command[0] == "forward":
        horizontal_position = horizontal_position + int(command[1])
    elif command[0] == "down":
        depth = depth + int(command[1])
    elif command[0] == "up":
        depth = depth - int(command[1])
    else:
        print("uh oh")
dive = horizontal_position * depth

print(f"Part 1: {dive}")
