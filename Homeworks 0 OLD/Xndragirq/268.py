import random
def input_num(message):
	while True:
		try:
			n = int(input(message))
			return n
		except ValueError:
			print("Mutqagreq tiv!")
def rand_arr(n = 5, a = 0, b = 5):
	arr = []
	for i in range(n):
		arr.append(random.randint(a,b))
	return arr
while True:
	n = input_num("Mutqagreq zangvaci erkarutyuny (0 - elq): ")
	if n is 0:
		print("Hajoxutyun!")
		break
	a = input_num("Mutqagreq random min: ")
	b = input_num("Mutqagreq random max: ")
	while b <= a:
		print("max chi karox linel poqr kam havasar min!")
		b = input_num("Mutqagreq random max: ")
	k = input_num("Mutqagreq 0ic tarber tiv: ")
	while k is 0:
		print("Mutqagreq 0ic tarber tiv!")
		k = input_num("Mutqagreq 0ic tarber tiv: ")
	arrX = rand_arr(n, a, b)
	arrY = rand_arr(n, a, b)
	print("Array X = ", arrX)
	print("Array Y = ", arrY)
	c = 0
	for i in range(n):
		if arrX[i] % k is 0:
			c += 1
		if arrY[i] % k is 0:
			c += 1
	print("Qanaky = ",c)