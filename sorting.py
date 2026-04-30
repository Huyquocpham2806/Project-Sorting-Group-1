import math
import sys

sys.setrecursionlimit(2000000)

def insertion_sort(a: list[int]) -> tuple[list[int], int]: #book 1
    n = len(a)
    comparison = 0

    comparison += 1 # lượt check đầu tiên cho cái khoảng để có thể bắt đầu vòng lặp (nếu vòng lặp không chạy được thì nó cũng đồng thời là lượt check kết thúc, còn
                    # không thì nó sẽ là lượt đầu tiên trong vòng lặp, còn lượt cuối vòng lặp sẽ đếm cho việc kết thúc) 
    for i in range (1, n):
        comparison += 1 # đếm for loop

        val = a[i]
        j = i

        if j > 0: # lượt check đầu tiên để bắt đầu vòng lặp while (lập luận tương tự như for)
            comparison += 2
        else:
            comparison += 1 

        while j > 0:
            comparison += 1
            
            if  a[j - 1] > val:
                comparison += 1

                a[j] = a[j - 1]
                j -= 1

            else:
                break
  

        a[j] = val

    return a, comparison 

def binary_search_position(a: list[int], left: int, right: int, x: int) -> tuple[int, int]: # hàm tìm vị trí để insert bằng binary search 
    comparison = 0

    comparison += 1 
    while left <= right:
        comparison += 2 # đếm cho while + key comparison

        mid = (left + right)//2
        
        if a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return left, comparison # do lúc nào xong thì cũng là số lớn hơn x

def binary_insertion_sort(a: list[int]) -> tuple[list[int], int]: #book 2 (page 82)
    n = len(a)
    comparison = 0

    comparison += 1
    for i in range (1, n):
        comparison += 1

        val = a[i]
        j = i

        position, comp = binary_search_position(a, 0, i - 1, val)
        comparison += comp

        comparison += 1
        while j > position:
            comparison += 1
            a[j] = a[j - 1]
            j -= 1
        
        a[j] = val
    
    return a, comparison

def bubble_sort(a: list[int]) -> tuple[list[int], int]: #đưa phần tử lớn về cuối # book 2 (page 106)
    n = len(a)
    comparison = 0

    comparison += 1
    for i in range (n):
        comparison += 2
        for j in range (n - i - 1):
            comparison += 2
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
        
    return a, comparison

def shaker_sort(a: list[int]) -> tuple[list[int], int]: #cocktail sort: giống như bubble sort nhưng sort từ 2 phía nên chạy tới giữa thì là xong #book 2 (page 109)
    n = len(a)
    left = 0
    right = n - 1
    comparison = 0
    swapped = True # biến để xem coi sau khi dò thì có lần nào swap không (nếu không thì có nghĩa là tất cả đều đúng vị trí)

    comparison += 1 
    while swapped:
        comparison += 1

        swapped = False

        comparison += 1
        for j in range (left, right):
            comparison += 2
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
                swapped = True
    
        right -= 1
        
        comparison += 1
        for j in range (right, left, -1):
            comparison += 2
            if a[j] < a[j - 1]:
                a[j - 1], a[j] = a[j], a[j - 1]
                swapped = True
        
        left += 1

        comparison += 1 
        if not swapped:
            break
    
    return a, comparison

def shell_sort(a: list[int]) -> tuple[list[int], int]: #shell sort với gap (8, 4, 2, 1) #book 2 (page 83)
    n = len(a)
    comparison = 0
    gaps = [8, 4, 2, 1]

    comparison += 1
    for gap in gaps:
        comparison += 2

        for i in range (gap, n):
            comparison += 1

            val = a[i]
            j = i
            
            if j - gap >= 0:
                comparison += 2
            else:
                comparison += 1
            
            while j - gap >= 0:
                comparison += 1

                if a[j - gap] > val:
                    comparison += 1

                    a[j] = a[j - gap]
                    j -= gap

                else:
                    break

            a[j] = val
    
    return a, comparison

def selection_sort(a: list[int]) -> tuple[list[int], int]: #book 2 (page 138)
    n = len(a)
    comparison = 0

    comparison += 1
    for i in range (n - 1):
        comparison += 2

        index = i

        for j in range (i + 1, n):
            comparison += 2
            if a[j] < a[index]:
                index = j
        
        a[index], a[i] = a[i], a[index]

    return a, comparison

def heapify(a: list[int], n , pos) -> int:
    is_heap = False
    k = pos
    comparison = 0

    if 2*k + 1 < n:
        comparison += 2
    else:
        comparison += 1
    
    while 2*k + 1 < n and not is_heap:
        comparison += 2

        j = 2*k + 1
        
        comparison += 1
        if j < n - 1:
            comparison += 1
            if a[j] < a[j + 1]:
                j += 1
        
        comparison += 1
        if a[k] >= a[j]:
            is_heap = True
        else:
            a[k], a[j] = a[j], a[k]
            k = j

    return comparison
    
def heap_sort(a: list[int]) -> tuple[list[int], int]: #book 1
    n = len(a)
    comparison = 0

    comparison += 1
    for i in range (n//2 - 1, -1, -1):
        comparison += 1
        comparison += heapify(a, n, i)
    
    comparison += 1
    for i in range (n - 1, 0 , -1):
        a[i], a[0] = a[0], a[i]
        comparison += heapify(a, i, 0)
        comparison += 1

    return a, comparison


def merge(a: list[int], left: int, right: int, mid: int) -> int:
    L = a[left: mid + 1]
    R = a[mid + 1: right + 1]
    i = 0
    j = 0
    k = left
    comparison = 0

    if i < len(L):
        comparison += 2
    else:
        comparison += 1

    while i < len(L) and j < len(R):
        comparison += 2

        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    
    comparison += 1
    while i < len(L):
        comparison += 1
        a[k] = L[i]
        i += 1
        k += 1
    
    comparison += 1
    while j < len(R):
        comparison += 1
        a[k] = R[j]
        j += 1
        k += 1

    return comparison

def merge_sort(a: list[int]) -> tuple[list[int], int]:
    return _merge_sort(a, 0, len(a) - 1)

def _merge_sort(a: list[int], left: int, right: int) -> tuple[list[int], int]: #book 1 (2.3)
    comparison = 0

    comparison += 1
    if left >= right:
        return a, 0

    mid = (left + right)//2

    _, left_comparison = _merge_sort(a, left, mid)
    _, right_comparison = _merge_sort(a, mid + 1, right)

    comparison += left_comparison
    comparison += right_comparison
    comparison += merge(a, left, right, mid)

    return a, comparison

def pivoting(a: list[int], left: int, right: int) -> tuple[int, int]: #the rightmost element as pivot
    comparison = 0
    pivot = a[right]
    i = left - 1

    comparison += 1
    for j in range (left, right):
        comparison += 2
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
        
    a[i + 1], a[right] = a[right], a[i + 1]

    return i + 1, comparison

def quick_sort(a: list[int]) -> tuple[list[int], int]:
    return _quick_sort(a, 0, len(a) - 1)

def _quick_sort(a: list[int], left: int, right: int) -> tuple[list[int], int]: #book 1
    comparison = 0

    comparison += 1
    if left >= right:
        return a, 0
    
    pivot_index, comps = pivoting(a, left, right)
    _, left_comparison = _quick_sort(a, left, pivot_index - 1)
    _, right_comparison = _quick_sort(a, pivot_index + 1, right)

    comparison += left_comparison + right_comparison + comps

    return a, comparison

def radix_sort(a: list[int]) -> tuple[list[int], int]: # d là độ dài của số lớn nhất # book 1 
    comparison = 0

    comparison += 1
    if not a:
        return a, comparison
    
    d = len(str(max(a)))
    buckets = [[] for _ in range (10)]
    exp = 0

    comparison += 1
    while exp < d:
        comparison += 2
        while len(a) > 0:
            comparison += 1
            val = a.pop()
            k = (val // (10**exp)) % 10
            buckets[k].append(val)

        comparison += 1
        for bucket in buckets:
            comparison += 2
            while len(bucket) > 0:
                comparison += 1
                a.append(bucket.pop())
        exp += 1

    return a, comparison

def counting_sort(a: list[int]) -> tuple[list[int], int]: #book 1
    n = len(a)
    comparison = 0

    comparison += 1
    if n == 0:
        return a, comparison

    c = [0]*(max(a) + 1)
    comparison += n - 1  

    b_id = [0]*n

    comparison += 1
    for x in a:
        comparison += 1
        c[x] += 1

    comparison += 1
    for i in range (1, len(c)):
        comparison += 1
        c[i] += c[i - 1]

    comparison += 1
    for j in range (n - 1, -1, -1):
        comparison += 1
        b_id[c[a[j]] - 1] = a[j]
        c[a[j]] -= 1
    
    return b_id, comparison  # n - 1 là số phép comparsion của phép max



def flash_sort(a: list[int]) -> tuple[list[int], int]: # https://www.neubert.net/Flapaper/9802n.htm
    n = len(a)
    comparison = 0

    comparison += 1
    if n <= 1:
        return a, 0

    # # Phần 1: phân bổ các buckets
    min_val = a[0]
    max_index = 0
    
    comparison += 1
    for i in range(1, n):
        comparison += 2

        if a[i] < min_val:
            min_val = a[i]
        else:
            comparison += 1
            if a[i] > a[max_index]:
                max_index = i

    comparison += 1
    if min_val == a[max_index]:
        return a, comparison  # nếu bằng nhau hết thì khỏi sort

    # chọn 0.45 vì theo paper thì nó phân chia tối ưu nhất
    comparison += 2 # xem lệnh làm tròn có sử dụng phép so sánh
    m = max(math.floor(0.45 * n), 1)
    L = [0] * m

    c = (m - 1) / (a[max_index] - min_val)

    comparison += 1
    for i in range(n):
        comparison += 2
        k = math.floor(c * (a[i] - min_val)) # cách tính xem phần tử thuộc về bucket nào
        L[k] += 1

    comparison += 1
    for i in range(1, m):
        comparison += 1
        L[i] += L[i - 1]

    # # Phần 2 : chuyển các số về buckets đúng của nó
    a[max_index], a[0] = a[0], a[max_index] # đổi phần tử lớn nhất lên đầu để chắc chắn lần swap đầu tiên thực hiện được
    
    move = 0 # track xem đã đưa được bao nhiêu phần tử về đúng bucket của nó
    j = 0 # track xem đang ở index nào
    k = m - 1 # track đang ở bucket nào (đặt k là bucket cuối để chắc chắn nó chỉ vào 1 bucket có phần tử, nếu chỉ vào 1 bucket 
              #không có phần tử thì while loop 2 sẽ gây ra lỗi bỏ qua phần tử)
    
    comparison += 1
    while move < n - 1: # n - 1 phần tử về đúng bucket rồi thì phần tử cuối cũng đúng (while loop 1)
        comparison += 2
        while j > L[k] - 1: #(while loop 2)
            comparison += 2
            j += 1
            k = math.floor(c * (a[j] - min_val))
            
        flash = a[j]
        
        comparison += 1
        while j != L[k]: # đặt các phần tử về đúng bucket của nó sao cho cái bucket mà j đang ở đã được đủ các phần tử (while loop 3)
            comparison += 2
            k = math.floor(c * (flash - min_val))
            L[k] -= 1
            a[L[k]], flash = flash, a[L[k]]
            move += 1

    a, comps = insertion_sort(a)
    comparison += comps

    return a, comparison

