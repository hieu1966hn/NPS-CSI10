Buổi 2: Giới thiệu về Thuật toán và Cấu Trúc Dữ Liệu
- Ý nghĩa của thuật toán và cấu trúc dữ liệu (CTDL)
- Mối quan hệ giữa thuật toán và cấu trúc dữ liệu
- CTDL sẵn có trong Python



Thuật toán và độ phức tạp: Độ phức tạp của thuật toán là thước đo độ hiệu quả của thuật toán dựa theo kích cỡ tập dữ liệu đầu vào.  


1.2 Độ phức tạp về không gian
- Độ phức tạp về không gian thể hiện lượng không gian nhớ mà thuật toán cần để xử lý.

**Ví dụ**: Đối với hai thuật toán trên, độ phức tạp về không gian là O(1), do thuật toán không sử dụng thêm bộ nhớ khi kích cỡ input tăng lên.  
Tuy nhiên, nếu ta dùng list để lưu các số từ 1 đến n và tính tổng, độ phức tạp về không gian sẽ là O(n)


- Biết được độ phức tạp giúp ta ước tính được thời gian chạy và lượng bộ nhớ cần thiết để thuật toán xử lý.  
  
Bảng sau thể hiện một số lớp về độ phức tạp của thuật toán và thời gian chạy ước tính trên thực tế: (zalo)



1.4 Tính Toán Độ Phức Tạp
- Độ phức tạp về không gian được tính theo lượng bộ nhớ thuật toán cần sử dụng.  
- Độ phức tạp về thời gian được tính theo số phép toán mà thuật toán phải xử lý.  
*Lưu ý*: Nếu số phép toán hoặc không gian lưu trữ không phụ thuộc vào độ lớn dữ liệu đầu vào, thuật toán có độ phức tạp là O(1)  
  
**Ví dụ**: Bài toán tìm số lớn thứ hai trong dãy số.


Độ phức tạp không gian:
- Thuật toán sử dụng mảng có n phần tử, các biến n, biggest, i/j , second: Như vậy độ phức tạp về không gian là O(n+4) được viết dưới dạng O(n).

Độ phức tạp về thời gian: 
- Thuật toán vừa rồi sử dụng 2 vòng lặp for: 
+ vòng lặp 1 lặp qua n phần tử danh sách, mỗi lần lặp thực hiện phép so sánh max và phép gán, tổng cộng thực hiện 2n phép toán.
+ vòng lặp 2 lặp qua n phần tử của danh sách, mỗi lần lặp thực hiện khoảng 2 phép so sánh và một phép gán, tổng cộng 3n phép toán.

Ngoài ra, thuật toán còn thực hiện 3 phép gán bên ngoài và một lệnh return, tổng cộng 4 phép toán
=> Như vậy độ phức tạp về thời gian của thuật toán này là O(2n + 3n + 4) = O(5n + 4). Tương tự như độ phức tạp về không gian, khi n rất lớn, ta viết O(5n +4) dưới dạng O(n).

===> Tổng kết: Thuật toán trên có độ phức tạp về thời gian là .... và độ phức tạp về không gian là ....