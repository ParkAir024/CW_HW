# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    return [item for item in a if item not in b]

# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(s):
    words = s.split()
    min_length = min(len(word) for word in words)
    return min_length

# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    if len(walk) == 10:
        counts = {'n': 0, 's': 0, 'e': 0, 'w': 0}
        for direction in walk:
            counts[direction] += 1
        return counts['n'] == counts['s'] and counts['e'] == counts['w']
    else:
        return False


# https://www.codewars.com/kata/558fc85d8fd1938afb000014
    
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    counts = {}
    
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    for num, count in counts.items():
        if count == 1:
            return num
        