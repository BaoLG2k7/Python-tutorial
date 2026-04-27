arr = [1, 2, 3, 4, 5]

max = arr[0] # cho rằng số đầu là lớn nhất

for x in arr: # chạy x lần lượt từ 0 đến 4
    if x > max: # nếu x lớn hơn lần lượt chạy từ đầu
        max = x # max bằng x

print(max)