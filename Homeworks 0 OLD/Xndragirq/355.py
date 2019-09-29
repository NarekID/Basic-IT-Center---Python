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
	a = input_num("Mutqagreq random min (qaranish): ")
	while a < 1000:
		a = input_num("Mutqagreq random min (qaranish): ")
	b = input_num("Mutqagreq random max (qaranish): ")
	while b <= a:
		print("max chi karox linel poqr kam havasar min!")
		b = input_num("Mutqagreq random max: ")
	while b > 9999:
		b = input_num("Mutqagreq random max (qaranish): ")
	k = input_num("Mutqagreq tiv: ")
	arr = rand_arr(n, a, b)
	print("Array1\t",arr)
	for i in range(n):
		if arr[i] >= 1000 and arr[i] <=9999:
			q1 = int(arr[i] / 1000)
			q2 = int(arr[i]/100) % 10
			q3 = int(arr[i]/10) % 10
			q4 = arr[i] % 10
			if q1 + q2 + q3 + q4 is k:
				print(arr[i], " position ", i)