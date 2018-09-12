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
    k = int(lines.pop(0).strip())
    n = int(lines.pop(0).strip())
    numbers = [ int(x) for x in lines.pop(0).strip().split(' ') ]
    return (k, n, numbers)


def get_upper_bound(n, numbers, lower_bound):
    upper_bound = lower_bound
    for i in range(0, n):
        for j in range(i+1, n):
            diff = numbers[j] - numbers[i]
            if diff > upper_bound:
                upper_bound = diff
    
    return upper_bound


def find_next_best_jump(k, n, numbers, start_index, routes):
    if start_index == n-1:
        routes[start_index] = (None, 0) # (next_index, reward)
        return (None, 0)

    
    best_jump_next_index = None
    best_jump_reward = 0
    for j in range(start_index+1, n):
        if numbers[j] - numbers[start_index] >= k:
            """
            if routes[j][1] >= best_jump_reward --> Competing jumps/hops are considered.
                                                --> i.e. individual jumps/hops are long,
                                                -->      skipping competing nodes
            
            if routes[j][1] > best_jump_reward  --> Competing jumps/hops are discarded.
                                                --> i.e. individual jumps/hops are short and immediate,
                                                -->      not skipping competing nodes
            
            Both are acceptable since the current node reward will be same either way.
            This method back propogates therefore there is not change in both the above setting
            however in forward propogation competing jumps/hops are important.
            See Dynamic programming for more details.
            """
            if routes[j][1] >= best_jump_reward:
                best_jump_next_index = j
                best_jump_reward = routes[j][1]

    routes[start_index] = (best_jump_next_index, 1 + best_jump_reward)
    return (best_jump_next_index, 1 + best_jump_reward)


def find_route(k, n, numbers):
    upper_bound = max(numbers) - min(numbers)
    if upper_bound < k:
        return (None, 0, None)

    # Adds latency which would most likely be not fruitful
    # upper_bound = get_upper_bound(n, numbers, -upper_bound)
    # if upper_bound < k:
    #     return(None, 0, None)

    
    best_reward = 0
    best_start_index = None
    routes = [ (None, 0) ] * n
    for i in range(n-1, -1, -1):
        next_index, reward = find_next_best_jump(k, n, numbers, i, routes)
        """
        if reward >= best_reward --> Competing routes are considered.
                                 --> The will give best route with minimum starting_index.
                                 --> i.e. the left most route.
        
        if reward > best_reward  --> Competing routes are discarded.
                                 --> This will give best route with maximum starting_index.
                                 --> i.e. the right most route.
        
        Both are acceptable since they do not change the best reward.
        """
        if reward >= best_reward:
            best_start_index = i
            best_reward = reward

    number_of_best_routes = len([ route for route in routes if route[1] == best_reward ])
    return (routes, best_start_index, 1 + best_reward, number_of_best_routes)


@timed
def main():
    with open("input.txt") as f:
        input_lines = f.readlines()

    k, n, numbers = sanitize_input(input_lines)

    routes, starting_index, reward, number_of_best_routes = find_route(k, n, numbers)

    best_route = []
    next_index = starting_index
    while (next_index != None):
        best_route.append(numbers[next_index])
        next_index = routes[next_index][0]

    print("\n BEST_ROUTE = {} \n STARTING_INDEX = {} \n REWARD = {}".format(best_route, starting_index, reward))


if __name__ == '__main__':
    main()

