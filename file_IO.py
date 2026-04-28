def write_to_file(filename, arr):
    with open(filename, 'w') as out:
        out.write(f"{len(arr)}\n")
        out.write(" ".join(map(str, arr)))

def read_from_file(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        data = list(map(int, f.readline().split()))

    return n, data