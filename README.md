# Project Sorting - Group 1

Project Data Structures & Algorithms - implement và benchmark 12 thuật toán sắp xếp:
Selection Sort, Insertion Sort, Binary Insertion Sort, Bubble Sort, Shaker Sort,
Shell Sort, Heap Sort, Merge Sort, Quick Sort, Counting Sort, Radix Sort, Flash Sort.

## Cấu trúc project

```
.
├── main.py                 # entry point cho CLI (Algorithm mode + Comparison mode)
├── sorting.py              # 12 thuật toán sắp xếp
├── generate_data.py        # sinh dữ liệu (sorted, nearly sorted, reversed, random)
├── measurement.py          # đo running time và đếm comparisons
├── file_IO.py              # đọc/ghi input.txt, output.txt
├── result.py               # in kết quả ra console
├── run_experiments.py      # chạy benchmark đầy đủ -> results.csv
└── visualize.py            # đọc results.csv -> 8 biểu đồ trong charts/
```

## Cài đặt

Yêu cầu: Python 3.10+

Cài các thư viện cần cho phần benchmark và vẽ biểu đồ:

```bash
pip install pandas matplotlib numpy
```

## Cách dùng

### 1. Chạy thuật toán theo CLI (theo yêu cầu đề bài)

**Algorithm mode** - chạy 1 thuật toán trên 1 input:

```bash
# Command 1: chạy trên file input
python main.py -a radix-sort input.txt -both

# Command 2: chạy trên data tự sinh với size + order
python main.py -a selection-sort 50 -rand -time

# Command 3: chạy trên cả 4 data orders
python main.py -a quick-sort 70000 -comp
```

**Comparison mode** - so sánh 2 thuật toán:

```bash
# Command 4: so sánh trên file input
python main.py -c heap-sort merge-sort input.txt

# Command 5: so sánh trên data tự sinh
python main.py -c quick-sort merge-sort 100000 -nsorted
```

Chi tiết các tham số:

| Tham số | Giá trị |
|---|---|
| Algorithm | `selection-sort`, `insertion-sort`, `binary-insertion-sort`, `bubble-sort`, `shaker-sort`, `shell-sort`, `heap-sort`, `merge-sort`, `quick-sort`, `counting-sort`, `radix-sort`, `flash-sort` |
| Input order | `-sorted`, `-nsorted`, `-rev`, `-rand` |
| Output param | `-time`, `-comp`, `-both` |

### 2. Chạy benchmark đầy đủ + vẽ biểu đồ (cho phần Report)

**Bước 1**: Chạy benchmark - sẽ sinh ra file `results.csv`

```bash
python run_experiments.py
```

⚠️ **Cảnh báo**: Lệnh này benchmark 12 thuật toán × 4 data orders × 6 data sizes
(10k, 30k, 50k, 100k, 300k, 500k). Vì các thuật toán O(n²) chạy rất chậm
trên Python với n=500k, **tổng thời gian có thể lên đến nhiều giờ đến hơn 1 ngày**.

Khuyến nghị:
- Cắm sạc, tắt sleep
- Chạy qua đêm hoặc cuối tuần
- Đừng tắt máy giữa chừng (sẽ mất kết quả)

**Bước 2**: Vẽ biểu đồ - sẽ sinh ra thư mục `charts/` chứa 8 file PNG

```bash
python visualize.py
```

Output:
- 4 line graphs (running time vs data size) - mỗi data order 1 hình
- 4 bar charts (comparisons vs data size) - mỗi data order 1 hình

Lệnh này chạy rất nhanh (vài giây) vì chỉ đọc CSV và vẽ.

## Format file results.csv

```
algorithm,data_order,data_size,running_time_ms,comparisons
selection-sort,Sorted,10000,..,..
...
```

Tổng cộng 288 dòng (12 × 4 × 6) + 1 dòng header.

## Ghi chú

- File `input.txt`, `output.txt`, `input_1.txt`, ..., `input_4.txt` được sinh
  tự động khi chạy main.py - đây là output theo yêu cầu đề bài.
- File `results.csv` và thư mục `charts/` chỉ tạo ra khi chạy phần benchmark.
- Radix sort và Counting sort là thuật toán non-comparison nên giá trị
  comparisons có thể bằng 0 hoặc rất nhỏ.

## Thành viên

Group 1 - DSA 25-26