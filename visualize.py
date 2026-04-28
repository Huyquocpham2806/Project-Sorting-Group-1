import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATA_ORDERS = ["Sorted", "Nearly Sorted", "Reversed", "Randomized"]
 
ALGORITHMS = [
    "selection-sort", "insertion-sort", "binary-insertion-sort",
    "bubble-sort", "shaker-sort", "shell-sort",
    "heap-sort", "merge-sort", "quick-sort",
    "counting-sort", "radix-sort", "flash-sort",
]

def plot_line(df, order, out_path):
    sub = df[df["data_order"] == order]

    plt.figure(figsize=(11, 6))

    colors = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
        "#393b79", "#637939"
    ]

    for i, algo in enumerate(ALGORITHMS):
        algo_df = sub[sub["algorithm"] == algo].sort_values("data_size")
        plt.plot(algo_df["data_size"], algo_df["running_time_ms"], marker="o", label=algo, color = colors[i])

    plt.title(f"Running time - {order} input")
    plt.xlabel("Data Size")
    plt.ylabel("Running time (ms)")
    plt.yscale("log")
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=9)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def plot_bar(df, order, out_path):
    sub = df[df["data_order"] == order]
    sizes = sorted(sub["data_size"].unique())
 
    n_algos = len(ALGORITHMS)
    bar_width = 0.8 / n_algos
    x = np.arange(len(sizes))

    colors = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
        "#393b79", "#637939"
    ]
 
    plt.figure(figsize=(13, 6))
    for i, algo in enumerate(ALGORITHMS):
        values = []
        for sz in sizes:
            row = sub[(sub["algorithm"] == algo) & (sub["data_size"] == sz)]
            values.append(row["comparisons"].iloc[0] if not row.empty else 0)
        offset = x - 0.4 + (i + 0.5) * bar_width
        plt.bar(offset, values, bar_width, label=algo, color = colors[i])
 
    plt.title(f"Number of Comparisons - {order} Input")
    plt.xlabel("Data Size")
    plt.ylabel("Comparisons")
    plt.yscale("log")
    plt.xticks(x, [f"{s:,}" for s in sizes])
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=9)
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def main():
    df = pd.read_csv("results.csv")
 
    os.makedirs("charts", exist_ok=True)
 
    for order in DATA_ORDERS:
        # Tạo tên file: "Nearly Sorted" -> "nearly_sorted"
        name = order.lower().replace(" ", "_")
        plot_line(df, order, f"charts/line_{name}.png")
        plot_bar(df, order, f"charts/bar_{name}.png")
 
 
if __name__ == "__main__":
    main()