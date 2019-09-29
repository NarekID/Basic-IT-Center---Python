def input_num(message):
	while True:
		try:
			n = int(input(message))
			return n
		except ValueError:
			print("Mutqagreq tiv!")
while True:
	n = input_num("Mutqagreq 0ic tarber tiv: ")
	if n is 0:
		print("Closing")
		break
	arr = []
	for i in range(1, n):
		if n % i is 0:
			arr.append(i)
	print("Array = ", arr)