"""Day 3: Binary Diagnostic."""
f = open("C:/Users/talee/Documents/GitHub/adventofcode_2021/inputs/day3.txt", "r")
data = [line.split()[0] for line in f]

for d in data:
    assert len(d) == 12

buffer = []
buffers = []
for x in range(len(data[0])):
    for num in data:
        buffer.append(num[x])
    buffers.append(buffer)
    buffer = []

one = 0
zero = 0
gamma = "0b"
epsilon = "0b"
for x in range(len(data[0])):
    for digit in buffers[x]:
        if digit == '1':
            one = one + 1
        elif digit == '0':
            zero = zero + 1
        else:
            print("uh oh")
    if one > zero:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    elif one < zero:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    one = 0
    zero = 0

gamma_rate = int(gamma, 2)
epsilon_rate = int(epsilon, 2)
power_consumption = gamma_rate * epsilon_rate
print(f"Part 1: {power_consumption}")