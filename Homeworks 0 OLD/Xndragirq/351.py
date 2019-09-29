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
	for i in range(1, n-1):
		if arr[i] > 0:
			isNeg1 = False
			isNeg2 = False
			if arr[i - 1] < 0:
				arr[i - 1] = -arr[i - 1]
				isNeg1 = True
			if arr[i + 1] < 0:
				arr[i + 1] = -arr[i + 1]
				isNeg2 = True
			if arr[i - 1] + arr[i + 1] > arr[i]:
				sm += arr[i] ** 2
				c += 1
			if isNeg1 is True:
				arr[i - 1] = -arr[i - 1]
			if isNeg2 is True:
				arr[i + 1] = -arr[i + 1]
	print("Mijin qarakusayiny = ", (sm/c) ** 0.5)