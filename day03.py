# Example
example01 = """987654321111111
811111111111119
234234234234278
818181911112111"""

answer01 = 357
answer02 = 3121910778619

data = example01.splitlines()

# Finds biggest number and its position 
def findBiggestRemaining(n_str):
    x = 0
    x_i = 0
    len_str = len(n_str)
    for i in range(0,len_str):
        if x < int(n_str[i]):
            x = int(n_str[i])
            x_i = i
    return (x, x_i)

# calculate joltage using substring searches
def calculateJoltage(n_str, count):
    result = ''
    offset = 0
    for i in range(0, count):
        # increase offset with position of next biggest remaining digit
        n_with_offset = n_str[offset:]
        # count how many digits are still required to be present until end
        remaining = count - i - 1
        # substring suffix that needs to be preserved
        n_available = n_with_offset[0 : len(n_with_offset) - remaining]
        x = findBiggestRemaining(n_available)
        # increase offset by found digit position
        offset += x[1] + 1
        # concat found digit to create final digit
        result += str(x[0])
    return int(result)

# sum joltage for given battery count
def solution(data, count):
    total = 0
    for n in data:
        total += calculateJoltage(n, count)
    return total

assert(answer01 == solution(data, 2))
assert(answer02 == solution(data, 12))

# Load and check real data
with open('input03.txt') as f:
    lines = f.read().splitlines()

print("Solution 01: " + str(solution(lines, 2)))
print("Solution 02: " + str(solution(lines, 12)))
