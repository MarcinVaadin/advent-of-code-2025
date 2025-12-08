example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

answer01 = 21

answer02 = 40

# Split into 2d array
def prepareData(text):
    return list(map(list, text.splitlines()))

# Mark all beams, count active splitters
def solution01(data):
    splitted = 0
    for i in range(1, len(data)):
        for j in range(0, len(data[i])):
            # beam present
            if data[i - 1][j] == '|' or data[i - 1][j] == 'S':
                # beam passing
                if data[i][j] == '.':
                    data[i][j] = '|'
                # beam split
                if data[i][j] == '^':
                    data[i][j - 1] = '|'
                    data[i][j + 1] = '|'
                    splitted += 1
    return splitted

assert(answer01 == solution01(prepareData(example)))

# Count weights of paths
# . . . . . . . S . . . . . . .
# . . . . . . . | . . . . . . . 1
# . . . . . . | ^ | . . . . . .
# . . . . . . 1 . 1 . . . . . . 2
# . . . . . | ^ | ^ | . . . . .
# . . . . . 1 . 2 . 1 . . . . . 4
# . . . . | ^ | ^ | ^ | . . . .
# . . . . 1 . 3 . 3 . 1 . . . . 8
# . . . | ^ | ^ | | | ^ | . . .
# . . . 1 . 4 . 3 3 1 . 1 . . . 13
# . . | ^ | ^ | | | ^ | ^ | . .
# . . 1 . 5 . 4 3 4 . 2 . 1 . . 20
# . | ^ | | | ^ | | . | | ^ | .
# . 1 . 1 5 4 . 7 4 . 2 1 . 1 . 26
# | ^ | ^ | ^ | ^ | x | | | ^ | 
# 1 . 2 .10 . 11. 11. 2 1 1.  1 40

# Utility for marking beams on diagram
def drawLines(data):
    for i in range(1, len(data)):
        for j in range(0, len(data[i])):
            # beam present
            if data[i - 1][j] == '|' or data[i - 1][j] == 'S':
                # beam passing
                if data[i][j] == '.':
                    data[i][j] = '|'
                # beam split
                if data[i][j] == '^':
                    data[i][j - 1] = '|'
                    data[i][j + 1] = '|'
    return data

# Calculates weight of given path based on parent splitters and direct beams
def getWeight(i, j, data):
    weight = 0
    # parent left active splitter
    if j > 0 and data[i - 1][j - 1] == '^' and data[i - 2][j - 1] != '.':
        weight += data[i - 2][j - 1]
    # parent right active splitter
    if j < len(data[i]) - 1 and data[i - 1][j + 1] == '^' and data[i - 2][j + 1] != '.':
        weight += data[i - 2][j + 1]
    # direct beam
    if data[i - 1][j] == '|' and data[i - 2][j] != '.':
       weight += data[i - 2][j]
    return weight

# Calculates all path weights and returns sum of final paths
def solution02(data):
    data = drawLines(data)
    # init with weight 1
    for j in range(0, len(data[0])):
        if data[0][j] == 'S':
            data[1][j] = 1
            break
    
    for i in range(3, len(data), 2):
        for j in range(0, len(data[i])):
            if data[i][j] == '|':
                data[i][j] = getWeight(i, j, data)
    
    last_i = len(data) - 1
    total = 0
    for j in range(0, len(data[last_i])):
        if data[last_i][j] != '.':
            total += data[last_i][j]
    return total
    
assert(answer02 == solution02(prepareData(example)))

# Load and check real data
with open('input07.txt') as f:
   lines = f.read()

print("Solution 01: " + str(solution01(prepareData(lines))))
print("Solution 02: " + str(solution02(prepareData(lines))))
