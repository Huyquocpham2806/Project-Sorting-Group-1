import csv
import os
import sys
import time
from generate_data import generate_data
from measurement import measure_time_comp

sys.setrecursionlimit(2_000_000)

OUTPUT_CSV = "results.csv"
CSV_FIELDS = ["algorithm", "data_order", "data_size",
              "running_time_ms", "comparisons"]
 
DATA_SIZES = [10_000, 30_000, 50_000, 100_000, 300_000, 500_000]

DATA_ORDERS = [
    ("-sorted",  "Sorted"),
    ("-nsorted", "Nearly Sorted"),
    ("-rev",     "Reversed"),
    ("-rand",    "Randomized"),
]
 
ALGORITHMS = [
    "selection-sort",
    "insertion-sort",
    "binary-insertion-sort",
    "bubble-sort",
    "shaker-sort",
    "shell-sort",
    "heap-sort",
    "merge-sort",
    "quick-sort",
    "counting-sort",
    "radix-sort",
    "flash-sort",
]

def main():
    rows = []

    for params, order_name in DATA_ORDERS:
        for size in DATA_SIZES:
            data = generate_data(size, params)

            for algo in ALGORITHMS:
                print(f"{algo} | {order_name} | n = {size}")
                duration, comp, _ = measure_time_comp(algo, data)

                rows.append({
                    "algorithm": algo, 
                    "data_order": order_name,
                    "data_size": size,
                    "running_time_ms": duration,
                    "comparisons": comp,
                })

    with open("results.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "algorithm", "data_order", "data_size",
                "running_time_ms", "comparisons"
            ])
            writer.writeheader()
            writer.writerows(rows)
    
 
if __name__ == "__main__":
    main()