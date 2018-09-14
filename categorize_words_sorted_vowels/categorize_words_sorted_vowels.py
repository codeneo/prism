from functools import wraps
from time import time


def timed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        duration = time() - start_time
        print("\n\nExecution time: {:.4f} seconds".format(duration))
        return result
    return wrapper


def sanitize_input(lines):
    t = int(lines.pop(0).strip())
    words = [ x.strip() for x in lines ]
    return (t, words)


def categorize(word, vowels):
    vowels_int_value = [ ord(v) for v in word if v in vowels ]
    if len(vowels_int_value) == 0:
        return "Good"
    if len(vowels_int_value) == 1:
        return "Bad"

    i = vowels_int_value.pop(0)
    ascending = False
    descending = False
    for j in vowels_int_value:
        if not ascending and j > i:
            ascending = True
        if not descending and j < i:
            descending = True
        if ascending and descending:
            return "Bad"
        i = j
    
    if ascending:
        return "Good"
    elif descending:
        return "Worst"
    else:
        return "Bad"

    return None


@timed
def main():
    with open("input.txt") as f:
        input_lines = f.readlines()

    number_testcases, words = sanitize_input(input_lines)

    vowels = "aeiou"
    for word in words:
        print("\n WORD = {} \n CATEGORY = {}".format(word, categorize(word, vowels)))


if __name__ == '__main__':
    main()

