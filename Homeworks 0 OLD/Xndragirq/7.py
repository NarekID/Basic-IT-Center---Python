import math
def input_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq tiv!")
while True:
	x = input_number("Mutqagreq X:\n")
	y = input_number("Mutqagreq Y:\n")
	a = (((((x ** 2) + (y ** 2)) ** 5) + 4) ** 7) + (math.sin(math.cos(x + y)))
	print("Patasxany = ", a, ", vortex X = ",x,", Y = ", y)