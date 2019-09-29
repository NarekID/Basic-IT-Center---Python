import random
def input_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Input a number!")
def create_array(n = 10, a = 1, b = 10):
	arr = []
	for i in range(n):
		arr.append(random.randint(a,b))
	return arr
while True:
	n = input_number("n (Default 10): ")
	if n is 0:
		print("Good Bye!")
		break
	mn = input_number("min (Default 1): ")
	mx = input_number("max (Default 10): ")
	while mx <= mn:
		mx = input("max is lower or equal min!")
		mx = input_number("max (Default 10): ")
	arr_2d = []
	for i in range(n):
		arr_2d.append(create_array(n, mn, mx))
	summ = 0
	for i in range(n):
		for j in range(n):
			print(arr_2d[i][j], end="\t")
			if i > j:
				summ += arr_2d[i][j]
		print("")
	print("sum = ", summ)