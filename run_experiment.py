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

ALL_ORDERS = {
    "-sorted":  "Sorted",
    "-nsorted": "Nearly Sorted",
    "-rev":     "Reversed",
    "-rand":    "Randomized",
}

 
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

def run_orders(order_to_run):
    rows = []

    for params, order_name in order_to_run:
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

    file_exists = os.path.exists(OUTPUT_CSV)

    with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            if not file_exists:
                writer.writeheader()
            writer.writerows(rows)

def main():
    
    if len(sys.argv) == 1:
        order_to_run = list(ALL_ORDERS.items())
    
    elif len(sys.argv) == 2:
        params = sys.argv[1]
        if params not in ALL_ORDERS:
            print(f"Lỗi: order không hợp lệ '{params}'")
            print(f"Các giá trị hợp lệ: {list(ALL_ORDERS.keys())}")
            return
        order_to_run = [(params, ALL_ORDERS[params])]
    
    else:
        print("Lỗi: chỉ nhận tối đa 1 tham số")
        return
 
    run_orders(order_to_run)    
 
if __name__ == "__main__":
    main()