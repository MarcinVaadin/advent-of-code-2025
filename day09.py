example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

answer01 = 50

def prepareData(text):
    data = []
    for line in str(text).splitlines():
        splitted = line.split(',')
        data.append((int(splitted[0]), int(splitted[1])))
    return data

data = prepareData(example)

def calculateArea(a, b):
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)

def calculateAreas(data):
    areas = []
    for i in data:
        for j in data:
            if i == j:
                continue
            areas.append(calculateArea(i, j))
    return areas

def solution01(data):
    areas = calculateAreas(data)
    return max(areas)

assert(answer01 == solution01(prepareData(example)))

def printData(data):
    print(data)
    max_x = 0
    max_y = 0
    for d in data:
        max_x = d[0] if d[0] > max_x else max_x
        max_y = d[1] if d[1] > max_y else max_y
    for y in range(0, max_y + 2):
        for x in range(0, max_x + 2):
            if (x, y) in data:
                print('#', end='')
            else:
                print('.', end='')
        print('')

printData(prepareData(example))

# Load and check real data
with open('input09.txt') as f:
   lines = f.read()

print("Solution 01: " + str(solution01(prepareData(lines))))
