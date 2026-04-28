arr = [1,2,3,4,5,6,7]

vitri = 0 # giả sử vị trí lớn nhất ban đầu là 0

for i in range(len(arr)):
    if arr[i] > arr[vitri]:
        vitri = i

print(vitri)
print(arr[vitri])