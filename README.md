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
├── run_experiment.py       # chạy benchmark -> results.csv
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

### 2. Chạy benchmark + vẽ biểu đồ (cho phần Report)

#### Bước 1: Chạy benchmark

`run_experiment.py` hỗ trợ 2 cách chạy:

**Cách A - Chạy hết 4 data orders cùng lúc:**

```bash
python run_experiment.py
```

⚠️ Cảnh báo: cách này có thể mất hơn 1 ngày để chạy xong (đặc biệt với
quick-sort trên data Sorted/Reversed sẽ rơi vào worst case O(n²)).

**Cách B - Chạy từng data order riêng (khuyến nghị):**

```bash
python run_experiment.py -sorted    # chỉ chạy data đã sorted
python run_experiment.py -nsorted   # chỉ chạy data nearly sorted
python run_experiment.py -rev       # chỉ chạy data reversed
python run_experiment.py -rand      # chỉ chạy data randomized
```

Mỗi lần chạy sẽ **ghi nối** kết quả vào `results.csv` (không ghi đè).
Nhờ đó có thể chạy nhiều lần cách quãng, gom đủ 4 orders.

Thời gian tham khảo cho từng order:
- `-rand`, `-nsorted`: ~10-20 giờ mỗi cái
- `-sorted`, `-rev`: ~25-50 giờ mỗi cái (do quick-sort worst case)

⚠️ Nếu muốn chạy lại từ đầu, **xóa file `results.csv` trước khi chạy**
để tránh dữ liệu bị trùng lặp.

Khuyến nghị khi chạy:
- Cắm sạc, tắt sleep
- Đóng các app nặng (Chrome, IDE)
- Chạy qua đêm hoặc lúc không dùng máy

#### Bước 2: Vẽ biểu đồ

```bash
python visualize.py
```

Sẽ sinh ra thư mục `charts/` chứa 8 file PNG:
- 4 line graphs (running time vs data size) - mỗi data order 1 hình
- 4 bar charts (comparisons vs data size) - mỗi data order 1 hình

Lệnh này chạy rất nhanh (vài giây) vì chỉ đọc CSV và vẽ. Có thể chạy bất cứ
lúc nào - kể cả khi mới có 1-2 orders trong CSV (các biểu đồ của orders
chưa có data sẽ trống).

## Format file results.csv

```
algorithm,data_order,data_size,running_time_ms,comparisons
selection-sort,Sorted,10000,..,..
...
```

Đầy đủ sẽ có 288 dòng (12 × 4 × 6) + 1 dòng header.

## Ghi chú

- File `input.txt`, `output.txt`, `input_1.txt`, ..., `input_4.txt` được sinh
  tự động khi chạy main.py - đây là output theo yêu cầu đề bài.
- File `results.csv` và thư mục `charts/` chỉ tạo ra khi chạy phần benchmark.
- Radix sort và Counting sort là thuật toán non-comparison nên giá trị
  comparisons có thể bằng 0 hoặc rất nhỏ.

## Thành viên

Group 1 - DSA 25-26