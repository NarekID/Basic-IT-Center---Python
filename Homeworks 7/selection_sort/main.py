arr = [5, 4, 345, 43, 5, 6, 9, -56, 0, -9, 57, 634]

print(arr)
for i in range(len(arr)):
    m = i
    for j in range(i+1, len(arr)):
        if arr[m] >= arr[j]:
            m = j
    arr[i], arr[m] = arr[m], arr[i]
print(arr)