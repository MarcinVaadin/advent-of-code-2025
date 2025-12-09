import math
from operator import itemgetter

example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

shortest_connections_count01_example = 10
expected01 = 40

shortest_connections_count01_task = 1000

expected02 = 25272

class Result(Exception):
    def __init__(self, message, a, b):
        super().__init__(message)
        self.a = a
        self.b = b

def prepareData(text):
    data = list()
    for line in str(text).splitlines():
        [x, y, z] = line.split(',')
        data.append((int(x), int(y), int(z)))
    return data

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

# calculate distances
def calculateDistances(data):
    distances = set()
    data_len = len(data)
    for i in range(0, data_len):
        for j in range(0, data_len):
            if i == j:
                continue
            # store in same order to eliminate duplicates
            start = i if i < j else j
            end = i if i >= j else j
            distances.add((start, end, distance(data[start], data[end])))
    return distances

# group N shortest connections into circuits
def groupIntoCircuits(sorted_by_distance, desired_connections_count, total_junctions):
    circuits = []
    for i in range(0, desired_connections_count):
        
        # throw result of second task
        if len(circuits) == 1 and len(circuits[0]) == total_junctions:
            raise Result('Finished', a, b)
        
        (a, b, dist) = sorted_by_distance[i]
        a_circuit = None
        b_circuit = None
        for circuit in circuits:
            if a_circuit == None and a in circuit:
                a_circuit = circuit
            if b_circuit == None and b in circuit:
                b_circuit = circuit

        # a and b in none circuits -> create new
        if a_circuit == None and b_circuit == None:
            circuits.append(set([a, b]))
            continue

        # a and b in same circuit -> do nothing
        if a_circuit == b_circuit:
            continue

        # a in circuit, b not -> add b to circuit
        if a_circuit != None and b_circuit == None:
            a_circuit.add(b)
            continue
        
        # a not in circuit, b in -> add a to circuit
        if a_circuit == None and b_circuit != None:
            b_circuit.add(a)
            continue

        # in different circuits -> join as one
        if a_circuit != None and b_circuit != None:
            b_circuit |= a_circuit
            circuits.remove(a_circuit)
            continue
    
    return circuits

def multiplyThreeBiggestCircuits(circuits):
    # get length of each circuit, sort
    circuits_lenghts = sorted(list(map(len, circuits)))
    total = 1
    # multiply biggest (last) three circuits
    for i in circuits_lenghts[-3:]:
        total *= i
    return total

def solution01(data, shortest_connection_count):
    distances = calculateDistances(data)
    sorted_by_distance = sorted(distances, key=itemgetter(2))
    circuits = groupIntoCircuits(sorted_by_distance, shortest_connection_count, len(data))
    return multiplyThreeBiggestCircuits(circuits)

answer01 = solution01(prepareData(example), shortest_connections_count01_example)
assert(answer01 == expected01)

# Load and check real data
with open('input08.txt') as f:
   lines = f.read()

print("Solution 01: " + str(solution01(prepareData(lines), shortest_connections_count01_task)))

data = prepareData(example)
try:
    solution01(data, 10000)
except Result as result:
    assert(expected02 == data[result.a][0] * data[result.b][0])

data = prepareData(lines)
try:
    solution01(data, 10000000)
except Result as result:
    print("Solution 02: " + str(data[result.a][0] * data[result.b][0]))
