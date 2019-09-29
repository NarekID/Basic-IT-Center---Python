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
	k = input_number("Mutqagreq 0ic mec tiv: ")
	while k <= 0:
		k = input_number("Mutqagreq 0ic mec tiv: ")
	arr = [0] * n
	s = 0
	count = 0
	for i in range(n):
		arr[i] = input_number("a["+str(i)+"] = ")
		while type(arr[i]) is not int:
			arr[i] = input_number("a["+str(i)+"] = ")
		if arr[i] % k is 0:
			s += arr[i] ** 2
			count += 1
	print("Mijin qarakusayiny = ", (s/count) ** 0.5) 