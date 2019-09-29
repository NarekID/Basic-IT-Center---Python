import math
def input_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq tiv!")
while True:
	a = input_number("Mutqagreq a = ")
	while a == 0:
		a = input_number("Mutqagreq 0ic tarber a = ")
	b = input_number("Mutqagreq b = ")
	while b == 0:
		b = input_number("Mutqagreq 0ic tarber b = ")
	c = input_number("Mutqagreq c = ")
	while c == 0:
		c = input_number("Mutqagreq 0ic tarber c = ")
	if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
		print("1")
	else:
		print("2")