import random
def input_num(message):
	while 1:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq tiv!")
def generate_password(n = 8, upperCases = False, numbers = False, symbols = False):
	password = ""
	if upperCases:
		if numbers:
			if symbols:
				for i in range(n):
					password += chr(random.randint(33, 126))
			else:
				for i in range(n):
					temp = random.randint(0,2)
					if temp is 0:
						password += chr(random.randint(48,57))
					elif temp is 1:
						password += chr(random.randint(65,90))
					elif temp is 2:
						password += chr(random.randint(97,122))
		else:
			if symbols:
				for i in range(n):
					temp = random.randint(0,1)
					if temp is 0:
						password += chr(random.randint(33,47))
					elif temp is 1:
						password += chr(random.randint(58,126))
			else:
				for i in range(n):
					temp = random.randint(0,1)
					if temp is 0:
						password += chr(random.randint(65,90))
					elif temp is 1:
						password += chr(random.randint(97,122))
	else:
		if numbers:
			if symbols:
				for i in range(n):
					temp = random.randint(0,1)
					if temp is 0:
						password += chr(random.randint(33,64))
					elif temp is 1:
						password += chr(random.randint(91,126))
			else:
				for i in range(n):
					temp = random.randint(0,1)
					if temp is 0:
						password += chr(random.randint(48,57))
					elif temp is 1:
						password += chr(random.randint(97,122))
		else:
			if symbols:
				for i in range(n):
					temp = random.randint(0,2)
					if temp is 0:
						password += chr(random.randint(33,47))
					elif temp is 1:
						password += chr(random.randint(58,64))
					elif temp is 2:
						password += chr(random.randint(91,126))
			else:
				for i in range(n):
					password += chr(random.randint(97,122))
	return password

while 1:
	n = input_num("Mutqagreq gaxtnabari erkarutyuny (0 - elq cragric): ")
	if n is 0:
		print("Hajoxutyun!")
		break
	if n < 0:
		print("Erkarutyuny chi karox liner bacasakan!")
		continue
	upperCases = -1
	while upperCases is not 0 and upperCases is not 1:
		upperCases = input_num("Gaxtnabary petq e parunaki mecatar tarer? (0 - voch, 1 - ayo): ")
	if upperCases is 0:
		upperCases = False
	elif upperCases is 1:
		upperCases = True
	numbers = -1
	while numbers is not 0 and numbers is not 1:
		numbers = input_num("Gaxtnabary petq e parunaki tiv? (0 - voch, 1 - ayo): ")
	if numbers is 0:
		numbers = False
	elif numbers is 1:
		numbers = True
	symbols = -1
	while symbols is not 0 and symbols is not 1:
		symbols = input_num("Gaxtnabary petq e parunaki symbol? (0 - voch, 1 - ayo): ")
	if symbols is 0:
		symbols = False
	elif symbols is 1:
		symbols = True
	password = generate_password(n, upperCases, numbers, symbols)
	print("\nDzer yntrutyunnery`")
	print("Erkarutyuny ", n)
	print("Mecatarer - ", upperCases)
	print("Tver - ", numbers)
	print("Simvolner - ", symbols)
	print("Dzer gaxtnabary - ", password, "\n")