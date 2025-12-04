example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

answer01 = 13
answer02 = 43

# Convert string to 2d array
def convertToMatrix(data):
    lines = str(data).splitlines()
    rows = len(lines)
    cols = len(lines[0])
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            matrix[i][j] = lines[i][j]
    return matrix

# count . around @, treat out of array as .
def countAvailableSpace(matrix, i, j, max_i, max_j):
    sum = 0
    for i_i in range(i - 1 , i + 2):
        for j_j in range(j - 1 , j + 2):
            # dont count itself
            if i_i == i and j_j == j:
                continue
            # count out of array as available space
            if i_i < 0 or j_j < 0 or i_i >= max_i or j_j >= max_j:
                sum += 1
                continue
            # count in array '.'
            if matrix[i_i][j_j] == '.':
                sum += 1
    return sum

# find @ to be removed where adjacent rolls < 4
# available space around @ must be >= 5 (total = 8)
def findToBeRemoved(matrix):
    max_i = len(matrix)
    max_j = len(matrix[0])
    to_be_removed = []
    for i in range(0, max_i):
        for j in range(0, max_j):
            if matrix[i][j] == '@':
                space = countAvailableSpace(matrix, i, j, max_i, max_j)
                if space > 4:
                    to_be_removed.append((i, j))
    return to_be_removed

# just count removal candidates
def solution01(data):
    matrix = convertToMatrix(data)
    return len(findToBeRemoved(matrix))

assert(answer01 == solution01(example))

def remove(data, to_be_removed):
    for x in to_be_removed:
        data[x[0]][x[1]] = '.'
    return data

# remove in loop until possible
def solution02(data):
    matrix = convertToMatrix(data)
    removed = 0
    while True:
        to_be_removed = findToBeRemoved(matrix)
        if len(to_be_removed) == 0:
            return removed
        matrix = remove(matrix, to_be_removed)
        removed += len(to_be_removed)

assert(answer02 == solution02(example))

# Load and check real data
with open('input04.txt') as f:
   lines = f.read()

print("Solution 01: " + str(solution01(lines)))
print("Solution 02: " + str(solution02(lines)))
