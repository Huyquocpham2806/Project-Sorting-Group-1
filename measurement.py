import time
from sorting import *

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

def measure_time_comp(algo, data):
    arr_to_sort = data.copy()

    start = time.perf_counter()
    sorted_arr, comp = ALGORITHM[algo](arr_to_sort)
    end = time.perf_counter()

    duration = (end - start)*1000

    return duration, comp, sorted_arr