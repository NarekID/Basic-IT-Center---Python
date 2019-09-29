def input_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq tiv!")
while True:
	n = input_number("Enter line count (0 - exit): ")
	while True: n < 0:
		n = input_number("Mutqagreq drakan tiv")
	if n == 0:
		print("Hajoxutyun!")
		break
	for i in range(1, n+1):
		print(n * " " + i * "* ")
		n -= 1