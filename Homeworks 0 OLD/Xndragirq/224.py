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
	k = input_number("Mutqagreq tiv: ")
	arr = [0] * n
	s = 0
	for i in range(n):
		arr[i] = input_number("a["+str(i)+"] = ")
		while type(arr[i]) is not int:
			arr[i] = input_number("a["+str(i)+"] = ")
		if arr[i] < 0:
			arr[i] = -arr[i] #gtnum enq bacardzak arjeqy, karelie ogtagorcel math abs()
		if arr[i] > k:
			s += arr[i] ** 3
	print("Xoranardneri gumary = ", s)