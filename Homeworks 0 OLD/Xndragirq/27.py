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
				if a - b == b - c:
					progresia = 1
			else:
				if a - c == c - b:
					progresia = 1
		else:
			if c - a == a - b:
				progresia = 1
	else:
		if b > c:
			if a > c:
				if b - a == a - c:
					progresia = 1
			else:
				if b - c == c - a:
					progresia = 1
		else:
			if c - b == b - a:
				progresia = 1
	if progresia == 1:
		print("True")
	else:
		print("False")