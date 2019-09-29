def input_int_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq bnakan tiv!")
def input_float_number(message):
	while True:
		try:
			i = float(input(message))
			return i
		except ValueError:
			print("Mutqagreq irakan tiv!")
while True:
	x = input_float_number("Mutqagreq x irakan tivy = ")
	n = input_int_number("Mutqagreq n bnakan tivy = ")
	while n <= 0:
		n = input_int_number("Mutqagreq n bnakan tivy = ")
	s = 0
	for i in range(n):
		print(i)
		s += (x ** (4 * i + 1)) / (4 * i + 1)
		print("Sum = ", s)