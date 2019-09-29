def input_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq tiv!")
while True:
	progresia = 0
	a = input_number("Mutqagreq A = ")
	b = input_number("Mutqagreq B = ")
	while b == a:
		b = input_number("Mutqagreq B, vory havasar che A-in = ")
	c = input_number("Mutqagreq C = ")
	while c == a or c == b:
		c = input_number("Mutqagreq C, vory havasar che A-in kam B-in = ")
	if a > b:
		if a > c:
			if b > c:
				print(a, b, c)
			else:
				print(a, c, c)
		else:
			print(c, a, b)
	else:
		if b > c:
			if a > c:
				print(b, a, c)
			else:
				print(b, c, a)
		else:
			print(c, b, a)