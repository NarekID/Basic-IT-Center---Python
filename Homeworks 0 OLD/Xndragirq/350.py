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
	if n < 3:
		print("Tvyal xndiry lucelu hamar petq e zangvac, arnvazn 3 elementov!")
		continue
	a = input_num("Mutqagreq random min: ")
	b = input_num("Mutqagreq random max: ")
	while b <= a:
		print("max chi karox linel poqr kam havasar min!")
		b = input_num("Mutqagreq random max: ")
	arr = rand_arr(n, a, b)
	print("Array1\t",arr)
	sm = 0
	c = 0
	for i in range(n-1, -1, -1):
		if arr[i] > 0:
			sm += arr[i] ** 2
			c += 1
			if c is 5:
				break
	print("Mijin qarakusayiny = ", (sm/c) ** 0.5)