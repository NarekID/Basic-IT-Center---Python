arr = []
for i in range(100, 1000):
	if int(i/100) + (int(i/10) % 10) + i % 10 is 9:
		arr.append(i)
print("Array = ", arr)