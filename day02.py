from math import ceil
import re

# Example
example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
answer1 = 1227775554
answer2 = 4174379265

# convert to array of ints
def prepareData(text):
    return list(map(int, str(text).replace('-',',').split(',')))

def solution(data, isInvalidFunc):
    sum = 0
    for i in range(0, len(data), 2):
        for n in range(data[i], data[i+1] + 1):
            if (isInvalidFunc(n)):
                sum += n
    return sum

# Checks if first half of string equals second half
def isInvalid01(n):
    n_str = str(n)
    n_len = len(n_str)
    n_len_half = int(n_len / 2)
    
    # skip odd lenght strings
    if (n_len % 2 != 0):
        return False

    return n_str[0:n_len_half] == n_str[n_len_half:]

# Checks for more than 2 pattern repetitions
def isInvalid02(n):
    n_str = str(n)
    n_len = len(n_str)
    n_len_half = ceil(n_len / 2)
    # create patterns from maximum half of string characters
    for i in range(0, n_len_half):
        pattern = fr"^(?:{n_str[0:i+1]}){{2,}}"
        if(re.fullmatch(pattern, n_str)):
            return True

    return False

# Test example data
assert(answer1 == solution(prepareData(example), isInvalid01))
assert(answer2 == solution(prepareData(example), isInvalid02))

# Load and check real data
with open('input02.txt') as f:
      lines = f.read()

print("Solution 01: " + str(solution(prepareData(lines), isInvalid01)))
print("Solution 02: " + str(solution(prepareData(lines), isInvalid02)))
