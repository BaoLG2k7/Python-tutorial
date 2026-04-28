arr = [1,2,3,4,5,6,7,8,9]

max = arr[0]
min = arr[0]

for x in arr:
    if x > max:
        max = x

for i in arr:
    if i < min:
        min = i 

print(max)
print(min)


