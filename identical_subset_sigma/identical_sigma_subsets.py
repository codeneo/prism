from functools import wraps
from itertools import combinations
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
    n, k = [ int(x) for x in lines.pop(0).strip().split(' ') ]
    numbers = [ int(x) for x in lines.pop(0).strip().split(' ') ]
    return (n, k, numbers)


def is_identical_sigma_subset(n, numbers, k):
    if n == k:
        return "YES"
    k_subsets = combinations(numbers, k)
    summation = sum(next(k_subsets))
    for subset in k_subsets:
        if sum(subset) != summation:
            return "NO"
    return "YES"


@timed
def main():
    with open("input.txt") as f:
        input_lines = f.readlines()
    
    number_testcases = int(input_lines.pop(0).strip())

    for i in range(number_testcases):
        n, k, numbers = sanitize_input(input_lines)
        print("\nTestcase [{}], Output: {}".format(i+1, is_identical_sigma_subset(n, numbers, k)))


if __name__ == '__main__':
    main()

