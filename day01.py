
# Example values and answer
example1 = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
answer1 = 3
answer2 = 6

# Parameters
dial_size = 100 # 0 .. 99
start = 50

# Convert input to array of ints
def prepareData(data):
    return map(int, str(data).replace('L', '-').replace('R', '').splitlines())

# Task - count when dial points 0
# dial size = 0 .. 99 => 100
# points 0 when sum % 100 = 0
def solution01(data):
    total = 0
    current = start
    for n in data:
        current += n
        if (current % dial_size == 0):
            total += 1
    return total

# Task - count how many times dial passed 0
def solution02(data):
    total = 0
    current = start
    for n in data:
        prev = current
        current += n
        for i in range(prev, current, 1 if n > 0 else -1):
            if (i % dial_size == 0):
                total += 1
    return total

# Test example data
assert(answer1 == solution01(prepareData(example1)))
assert(answer2 == solution02(prepareData(example1)))  

# Load and check real data
with open('input01.txt') as f:
      lines = f.read()

print("Solution 01: " + str(solution01(prepareData(lines))))
print("Solution 02: " + str(solution02(prepareData(lines))))
