"""Day 1: Sonar Sweep."""
f = open("C:/Users/talee/Documents/GitHub/adventofcode_2021/inputs/day1.txt", "r")
data = [int(line) for line in f]

increased = 0
for x in range(1, len(data)):
    if data[x] > data[x-1]:
        increased = increased + 1
        
print(f"Part 1: {increased}")

numsum = []
for x in range(2, len(data)):
    numsum.append(data[x] + data[x-1] + data[x-2])

increased_new = 0
for x in range(1, len(numsum)):
    if numsum[x] > numsum[x-1]:
        increased_new = increased_new + 1

print(f"Part 2: {increased_new}")
