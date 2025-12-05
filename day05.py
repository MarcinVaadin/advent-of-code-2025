example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

answer01 = 3
answer02 = 14

# Parse input data into ([(x, y)], [z])
def prepareData(text):
    lines = str(text).splitlines()
    fresh = []
    ingredients = []
    for line in lines:
        if line == '':
            continue
        split = line.split('-')
        # fresh
        if (len(split) == 2):
            fresh.append((int(split[0]), int(split[1])))
        else:
            ingredients.append(int(line))
    return (fresh, ingredients)

# Check if ingredient is in any fresh set
def isFresh(fresh, ingredient):
    for f in fresh:
        if f[0] <= ingredient and ingredient <= f[1]:
            return True
    return False

# Count fresh
def solution01(data):
    fresh = data[0]
    ingredients = data[1]
    total = 0
    for ingredient in ingredients:
        if isFresh(fresh, ingredient):
            total += 1
    return total

# Utilities for simplifying sets of fresh
def intersects(a, b):
    return (b[0] <= a[0] and a[0] <= b[1]) or (b[0] <= a[1] and a[1] <= b[1])
def contains(a, b):
    return (a[0] <= b[0] and a[1] >= b[1])
def union(a, b):
    return (min(a[0], b[0]), max(a[1], b[1]))

# Simplify set using above utility methods
def clean_intersections(data):
    clean = []
    cleaned = False
    for d in data:
        to_be_unioned = None
        for c in clean:
            if intersects(d, c) or contains(d, c) or contains(c, d):
                to_be_unioned = d
                break
        if to_be_unioned == None:
            clean.append(d)
        else:
            cleaned = True
            clean.remove(c)
            clean.append(union(c, d))
    return (clean, cleaned)

# Simplify until possible, count totals
def solution02(data):
    fresh = data[0]
    cleaned = []
    while True:
        (clean, intersecting_found) = clean_intersections(fresh)
        if intersecting_found == False:
            cleaned = clean
            break
        else:
            fresh = clean
    
    total = 0
    for c in cleaned:
        total += (c[1] - c[0] + 1)

    return total

assert(answer01 == solution01(prepareData(example)))
assert(answer02 == solution02(prepareData(example)))

# Load and check real data
with open('input05.txt') as f:
   lines = f.read()

print("Solution 01: " + str(solution01(prepareData(lines))))
print("Solution 02: " + str(solution02(prepareData(lines))))