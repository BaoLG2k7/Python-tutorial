n = int(input("Nhập số: "))

attemps = 0 # Đếm số lần chia được 

# Chỉ khi n chia hết cho 2 dư 0 thì tiếp tục 

while n % 2 == 0: 
    n = n // 2       # Chia n cho 2 
    attemps += 1     # Tăng số lần chia 

print("Số lần chia được cho 2 là:", attemps)