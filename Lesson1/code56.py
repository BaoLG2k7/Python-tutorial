n = int(input("Nhập số lượng: "))
nums = []

for i in range(n):
    x = int(input("Nhập số: "))
    nums.append(x)

total = 0
for num in nums:
    total += num

print("Tổng là:", total)
