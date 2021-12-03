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

"""Part 2.
forward: add to horizontal position
forward: add aim multiplied by amount to depth
down: add to aim
up: subtract from aim
new dive: total horizontal position multiplied by total depth
"""

horizontal_position_new = 0
depth_new = 0
aim = 0
for command in commands:
    if command[0] == "forward":
        horizontal_position_new = horizontal_position_new + int(command[1])
        depth_new = depth_new + (aim * int(command[1]))
    elif command[0] == "down":
        aim = aim + int(command[1])
    elif command[0] == "up":
        aim = aim - int(command[1])
    else:
        print("uh oh")
dive_new = horizontal_position_new * depth_new

print(f"Part 2: {dive_new}")