from functools import wraps
from time import time
import multiprocessing as mp


def timed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        duration = time() - start_time
        print("\n\nExecution time: {:.4f} seconds".format(duration))
        return result
    return wrapper


def get_batches(number, max_size=1000):
    low = 1
    batches = []
    for i in range(1, max_size):
        high = int(i/max_size * number)
        if low <= high:
            batches.append( (low, high) )
            low = high + 1

    batches.append( (low, number) )
    return batches


def count_common_factors(first, second, low, high):
    num_factors = 0
    for i in range(low, high + 1):
        if (first % i == 0) and ( second % i == 0):
            num_factors += 1

    return num_factors


@timed
def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    minimum_number = min(first_number, second_number)

    batches = get_batches(number=minimum_number, max_size=1000)

    pool = mp.Pool(processes=8)

    batch_factors = []
    for batch in batches:
        low, high = batch
        batch_factors.append(pool.apply(count_common_factors, args=(first_number, second_number, low, high)))

    num_factors = sum(batch_factors)

    print("\n FIRST_NUMBER = {} \n SECOND_NUMBER = {} \n NUMBER_OF_COMMON_FACTORS = {}" \
            .format(first_number, second_number, num_factors))


if __name__ == '__main__':
    main()

