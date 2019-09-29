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
	a = (((2 ** x) - 5) / ((3 ** y) + 2)) + math.log2(((math.fabs(x) + 1) ** 4) + y ** 2)
	print("Patasxany = ", a, ", vortex X = ",x,", Y = ", y)