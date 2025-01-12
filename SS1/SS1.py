n = int(input("Nhập số nguyên n có 4 chữ số: "))

# kiểm tra điều kiện n có 4 chữ số 
if 1000 <= n <= 9999:
    a = n // 1000 # chữ số hàng nghìn
    b = (n // 100) % 10 # chữ số hàng trăm
    c = (n // 10) % 10 # chữ số hàng chục
    d = n % 10 # chữ số hàng đơn vị

# Tính tổng
tong = a + b + c + d 

# in kết quả
print('Tổng các chữ số trong số', n, "là:", tong)
