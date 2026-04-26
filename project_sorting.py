import argparse
import random
import time
import sys
import os
from sorting import * 
from file_IO import *
from generate_data import *
from measurement import *
from result import *

# Ý nghĩa của các biến

# algo: thuật toán được sử dụng
# params: tham số truyền vào
# size: kích thước của input data
# out_param: tham số đầu ra của đề yêu cầu (-comp, -time, hoặc -both)
# order: cách sắp xếp của kiểu dữ liệu (-sorted, -nsorted, -rev, -rand)
# data: dữ liệu từ file input

ALGORITHM = {
    "selection-sort": selection_sort,
    "insertion-sort": insertion_sort,
    "bubble-sort": bubble_sort,
    "shaker-sort": shaker_sort,
    "shell-sort": shell_sort,
    "heap-sort": heap_sort,
    "merge-sort": merge_sort,
    "quick-sort": quick_sort,
    "counting-sort": counting_sort,
    "radix-sort": radix_sort,
    "flash-sort": flash_sort,
    "binary-insertion-sort": binary_insertion_sort
}

def main():
    parser = argparse.ArgumentParser(description = "Nhóm 1 - Sorting project")
    grp = parser.add_mutually_exclusive_group(required = True)
    grp.add_argument('-a', nargs = argparse.REMAINDER, help='Algorithm Mode')
    grp.add_argument('-c', nargs = argparse.REMAINDER, help='Comparison Mode')

    args = parser.parse_args()

    if args.a:
        algorithm_mode(args.a)
    else:
        comparison_mode(args.c)

def algorithm_mode(params):
    n = len(params)
    algo = params[0]
    input_file, order = None, None 

    if n == 3:
        # Command 1:
        if not params[1].isdigit():
            input_file = params[1]
            out_param = params[2]
            size, data = read_from_file(input_file)
        else:
        # Command 3
            size = int(params[1])
            out_param = params[2]
            run_cm3(algo, size, out_param)
            return

    # Command 2
    elif n == 4:
        size = int(params[1])
        order = params[2]
        out_param = params[3]
        data = generate_data(size, order)
        write_to_file("input.txt", data)
    else:
        print("Lỗi: Không đủ số lượng tham số cho Algorithm mode")

    duration, comp, sorted_arr = measure_time_comp(algo, data)
    write_to_file("output.txt", sorted_arr)
    print_algo_result(algo, size, duration, comp, out_param, input_file, order)

def comparison_mode(params):
    n = len(params)
    algo1, algo2 = params[0], params[1]
    input_file, order = None, None 

    # Command 4
    if n == 3:
        input_file = params[2]
        size, data = read_from_file(input_file)
    # Command 5
    elif n == 4:
        size, order = int(params[2]), params[3]
        data = generate_data(size, order)
        write_to_file("input.txt", data)
    else:
        print("Lỗi: Không đủ số lượng tham số cho Algorithm mode")

    d1, c1, _ = measure_time_comp(algo1, data)
    d2, c2, _ = measure_time_comp(algo2, data)

    print_comp_result(algo1, algo2, d1, c1, d2, c2, size, order, input_file)

if __name__ == "__main__":
    main()