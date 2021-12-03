"""Day 1: Sonar Sweep."""
f = open("C:/Users/talee/Documents/GitHub/adventofcode_2021/inputs/day1.txt", "r")
data = [int(line) for line in f]

increased = 0
for x in range(1, len(data)):
    if data[x] > data[x-1]:
        increased = increased + 1
        
print(increased)