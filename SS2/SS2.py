## Độ phức tạp về thời gian
# Độ phức tạp về thời gian thể hiện số phép toán mà thuật toán phải xử lý, 
# từ đó ảnh hưởng đến thời gian thi hành của thuật toán.  
  
# **Ví dụ**: Bài toán tính tổng các số nguyên từ 1 đến n (n > 1)

# METHOD 1: Using a loop | Time complexity O(n)
def cal_sum_n_v1(num):
    result = 0
    for i in range(num+1):
        result += i
    return result

# print(cal_sum_n_v1(5))

# METHOD 2: Using a math equation | Time complexity O(1)
def cal_sum_n_v2(num):
    result = (num + 1) * num // 2
    return result

# print(cal_sum_n_v2(5))


## Tính thời gian thực hiện của 2 thuật toán trên:
import time
import math

def cal_time(func):
    start_time = time.time() # trả về thời gian hiện tại tính bằng giây. Lưu lại thời gian hiện tại, dùng làm mốc để tính toán thời gian chạy của hàm func.
    result = func() #  Kết quả trả về của hàm func được lưu vào biến result. (phải là 1 hàm ko tham số)
    real_time = time.time() - start_time # time.time() sẽ được gọi lại để lấy thời gian hiện tại.
    return real_time, result


BIG_NUMS = {'ONE MILLION': 1000000, 'TEN MILLION': 10000000, 'ONE HUNDRED MILLION': 100000000}

# print(BIG_NUMS.items())



# for name, num in BIG_NUMS.items():
#     print("Execution time for {} numbers:".format(name))
#     time1, res1 = cal_time(lambda: cal_sum_n_v1(num))
#     time2, res2 = cal_time(lambda: cal_sum_n_v2(num))
#     print("- O(n) algorithm: {} secs | result = {}".format(time1, res1))
#     print("- O(1) algorithm: {} secs | result = {}".format(time2, res2))
#     print()


## 1.2 Độ phức tạp về không gian
# Độ phức tạp về không gian thể hiện lượng không gian nhớ mà thuật toán cần để xử lý.


# METHOD 3: Using a list for storing numbers | Space complexity O(n)
def cal_sum_n_v3(num):
    number_list = [i for i in range(num+1)]
    result = 0
    for i in number_list:
        result += i
    return result

cal_sum_n_v3(5)



## Bài toán tìm số lớn thứ 2 trong dãy
arr = [4, 6, 2, 6, 1, 8, -1, -10, 0]

def find_second_biggest(arr):
    # tìm số lớn nhất
    biggest = arr[0]
    for i in arr:
        biggest = max(biggest, i)
        
    # Tìm số lớn thứ 2
    second = None
    for j in arr:
        if j == biggest:
            continue
        if second == None:
            second = j
        else: 
            second = max(j, second)
    return second

print(find_second_biggest(arr))
