n = int(input("Nhập số n:"))

if n < 0:
    print("Invalid")
else:
    sum = 0
    for i in range(1, n + 1): # chạy i trong khoảng số n
        sum += i # mỗi lần chạy là cộng i 
    print(sum) 