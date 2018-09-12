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


@timed
def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    minimum_number = min(first_number, second_number)

    count_common_factors = 0
    for i in range(1, minimum_number + 1):
        if (first_number % i == 0) and (second_number % i == 0):
            count_common_factors += 1

    print("\n FIRST_NUMBER = {} \n SECOND_NUMBER = {} \n NUMBER_OF_COMMON_FACTORS = {}" \
            .format(first_number, second_number, count_common_factors))


if __name__ == '__main__':
    main()

