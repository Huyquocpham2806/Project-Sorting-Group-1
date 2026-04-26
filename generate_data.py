import random

def generate_data(size, order):
    if order == "-rand":
        return [random.randint(0, size-1) for _ in range(size)]
    elif order == "-sorted":
        return list(range(size))
    elif order == "-nsorted":
        arr = list(range(size))
        for _ in range(100):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    elif order == "-rev":
        return list(range(size, 0, -1))