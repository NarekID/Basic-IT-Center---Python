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
	x = input_num("Mutqagreq mijakayqi skizby (0ic - n-1): ")
	while x >= n-1:
		print("Mijakayqy petq e poqr lini erkarutyunic!")
		x = input_num("Mutqagreq mijakayqi skizby (0ic - n-1): ")
	y = input_num("Mutqagreq mijakayqi verjy (1ic - n-1): ")
	while y <= x or y > n-1:
		print("Mijakayqi verjy chi karox linel poqr skzbnaketic kam zangvacic durs!")
		y = input_num("Mutqagreq mijakayqi verjy (1ic - n-1): ")
	arr = rand_arr(n, a, b)
	print(arr)
	c = 0
	for i in range(n):
		if i > x and i < y:
			c += 1
	print("Qanaky = ", c)