arr = []
for i in range(100, 1000):
	if (int(i/10) % 10) is i % 10:
		arr.append(i)
print("Array = ", arr)