arr = []
for i in range(10, 100):
	if (int(i / 10) + (i % 10)) > 5:
		arr.append(i)
print("Array = ", arr)