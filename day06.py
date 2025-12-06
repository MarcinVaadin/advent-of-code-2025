import re

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

answer01 = 4277556
answer02 = 3263827

# Converts input text ints and operators
def prepareData(text):
    lines = str(text).splitlines()
    lines_len = len(lines)
    data = []
    for i in range(0, lines_len - 1):
        data.append(list(map(int, lines[i].split())))
    return (data, lines[lines_len - 1].split())

def solution01(data):
    (numbers, operators) = data
    rows = len(numbers)
    columns = len(numbers[0])
    total = 0
    for i in range(0, columns):
        operator = operators[i]
        total_col = 0 if operator == '+' else 1
        for j in range(0, rows):
            number = numbers[j][i]
            total_col = (total_col + number) if operator == '+' else (total_col * number)
        total += total_col
    return total

assert(answer01 == solution01(prepareData(example)))


# Calculate width of each column
def calculateColumnWidths(operators_str):
    pattern = '[\\+\\*]{1}[ ]+'
    xs = re.findall(pattern, operators_str)
    widths = []
    for x in xs:
        widths.append(len(x) - 1)
    # add +1 to last column width as there is no space at the end of line
    widths[len(widths) - 1] = widths[len(widths) - 1] + 1
    return widths

def splitLineIntoColumns(line, column_widths):
    splitted = []
    offset = 0
    for width in column_widths:
        splitted.append(line[offset : offset + width])
        offset += width + 1
    return splitted

def prepareData02(text):
    lines = str(text).splitlines()
    lines_len = len(lines)
    column_widths = calculateColumnWidths(lines[lines_len -1])
    matrix = []
    for line in lines:
        matrix.append(splitLineIntoColumns(line, column_widths))
    return matrix

def calculateColumn(numbers, operator):
    column_width = len(numbers[0])
    is_sum = str(operator).find('+') != -1
    new_numbers = []
    for i in range(0, column_width):
        new_number = ''
        for j in range(0, len(numbers)):
            new_number += numbers[j][i]
        new_numbers.append(new_number)
    total = 0 if is_sum else 1
    for n in new_numbers:
        total = (total + int(n)) if is_sum else (total * int(n))
    return total

def solution02(data):
    operators = data[len(data) - 1]
    total = 0
    for j in range(0, len(data[0])):
        numbers = []
        for i in range(0, len(data) - 1):
            numbers.append(data[i][j])
        total += calculateColumn(numbers, operators[j])
    return total

assert(answer02 == solution02(prepareData02(example)))

# Load and check real data
with open('input06.txt') as f:
   lines = f.read()

print("Solution 01: " + str(solution01(prepareData(lines))))

print("Solution 02: " + str(solution02(prepareData02(lines))))