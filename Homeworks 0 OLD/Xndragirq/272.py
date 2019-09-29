import random
def input_num(message):
	while True:
		try:
			n = int(input(message))
			return n
		except ValueError:
			print("Mutqagreq tiv!")
def rand_str_arr(n = 5):
	arr = []
	for i in range(n):
		arr.append(chr(random.randint(0,25) + 97))
	return arr
while True:
	n = input_num("Mutqagreq zuyg erkarutyuny (0 - elq): ")
	if n is 0:
		print("Hajoxutyun!")
		break
	while n % 2 is 1:
		print("Mutqagrac tivy zuyg che!")
		n = input_num("Mutqagreq zuyg erkarutyuny (0 - elq): ")
	arr = rand_str_arr(n)
	print("Array = ", arr)
	c = 0
	for i in range(n):
		if 'b' in arr[i]:
			c += 1
	if c >= n/2:
		t = True
	else:
		t = False
	print(t)