from itertools import izip, count
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


def find_sum_of_tastes(word, vowels):
    word_length = len(word)
    tastes = ( (word_length - i) * (i + 1) for i, j in izip(count(), word) if j in vowels )
    return sum(tastes)


@timed
def main():
    with open("input.txt") as f:
        input_lines = f.readlines()

    number_testcases, words = sanitize_input(input_lines)

    vowels = "aAeEiIoOuU"
    for word in words:
        print("\n CHOCOLATE = {} \n TOTAL_SUM = {}".format(word, find_sum_of_tastes(word, vowels)))


if __name__ == '__main__':
    main()

