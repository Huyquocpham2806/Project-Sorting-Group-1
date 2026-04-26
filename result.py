from generate_data import * 
from measurement import *
from file_IO import *

def print_algo_result(algo, size, duration, comparison, out_param, input_file = None, order = None):
    ORDER_NAMES = {
        "-rand": "Randomize",
        "-nsorted": "Nearly Sorted",
        "-sorted": "Sorted",
        "-rev": "Reversed"
    }

    print("ALGORITHM MODE")
    print(f"Algorithm: {algo}")

    if input_file:
        print(f"Input file: {input_file}")
    
    print(f"Input size: {size}")

    if order:
        print(f"Input order: {ORDER_NAMES.get(order, order)}")

    print("-"*20)

    if out_param in ["-time", "-both"]:
        print(f"Running time: {duration:.3f} ms")
    
    if out_param in ["-comp", "-both"]:
        print(f"Comparisons: {comparison}")


def print_comp_result(algo1, algo2, d1, c1, d2, c2, size, order= None, input_file = None):
    ORDER_NAMES = {
        "-rand": "Randomize",
        "-nsorted": "Nearly Sorted",
        "-sorted": "Sorted",
        "-rev": "Reversed"
    }

    print(f"COMPARE MODE")
    print(f"Algorithm: {algo1} | {algo2}")

    print(f"Input size: {size}")
    if order:
        print(f"Input order: {ORDER_NAMES.get(order, order)}")
    if input_file:
        print(f"Input file: {input_file}")

    print("-"*20)

    print(f"Running time: {d1} | {d2}")
    print(f"Comparisons: {c1} | {c2}")

def run_cm3(algo, size, out_param):
    ORDER_NAMES = {
        "-rand": "Randomize",
        "-nsorted": "Nearly Sorted",
        "-sorted": "Sorted",
        "-rev": "Reversed"
    }
    types = ["-rand", "-nsorted", "-sorted", "-rev"]
    print(f"ALGORITHM MODE")
    print(f"Algorithm: {algo}")
    print(f"Input size: {size}\n")
 
    for i, order in enumerate(types):
        data = generate_data(size, order)
        write_to_file(f"input_{i+1}.txt", data)
        duration, comp, _ = measure_time_comp(algo, data)
 
        print(f"Input order: {ORDER_NAMES[order]}")
        print("-" * 20)
        if out_param in ["-time", "-both"]:
            print(f"Running time: {duration:.3f} ms")
        if out_param in ["-comp", "-both"]:
            print(f"Comparisons: {comp}")
        print()