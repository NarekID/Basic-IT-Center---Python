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
	if n < 0:
		print("Esrkarutyuny chi karox linel bacasakan!")
		continue
	a = input_num("Mutqagreq random min: ")
	b = input_num("Mutqagreq random max: ")
	while b <= a:
		print("max chi karox linel poqr kam havasar min!")
		b = input_num("Mutqagreq random max: ")
	arr = []
	for i in range(n):
		arr.append(rand_arr(n, a, b))
	for i in range(n):
		for j in range(n):
			print(arr[i][j], end="\t")
		print()
	print()
	c = 0
	sum1 = 0
	for i in range(n):
		for j in range(i+1):
			print(arr[i][j], end="\t")
			if arr[i][j] % 2 is 0:
				sum1 += arr[i][j] ** 2
				c += 1
		print()
	print("Gumary = ", sum1)
	print("Qanaky = ", c)
	print("Mijin qarakusayiny = ", (sum1/c) ** 0.5)