def input_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq tiv!")
while True:
	n = input_number("Mutqagreq zangvaci erkarutyuny (0 - elq cragric): ")
	while n < 0:
		print("Mutqagreq drakan tiv!")
		n = input_number("Mutqagreq zangvaci erkarutyuny (0 - elq cragric): ")
	if n is 0:
		print("Hajoxutyun!")
		break
	arr = [0] * n
	mul = 1
	for i in range(n):
		arr[i] = input_number("a["+str(i)+"] = ")
		while type(arr[i]) is not int:
			arr[i] = input_number("a["+str(i)+"] = ")
		if arr[i] - i > 0:
			mul *= arr[i]
	print("Artadryaly = ", mul)