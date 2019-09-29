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
	count = 0
	for i in range(n):
		changed = False
		arr[i] = input_number("a["+str(i)+"] = ")
		while type(arr[i]) is not int:
			arr[i] = input_number("a["+str(i)+"] = ")
		if arr[i] < 0:
			arr[i] = -arr[i] #gtnum enq bacardzak arjeqy, karelie ogtagorcel math abs()
			changed = True
		if arr[i] < k:
			count += 1
	print("Qanaky = ", count)