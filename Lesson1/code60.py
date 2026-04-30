n = int(input("Nhập số n:"))

dem = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        dem = dem + 1

print(dem)



