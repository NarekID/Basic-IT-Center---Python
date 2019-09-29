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
	arrX = rand_arr(n, a, b)
	arrY = rand_arr(n, a, b)
	print("Array X = ", arrX)
	print("Array Y = ", arrY)
	sm = 0
	for i in range(n):
		if i % 2 is 0:
			sm += arrX[i]
		elif i % 2 is 1:
			sm += arrY[i]
	print("Gumary = ", sm)