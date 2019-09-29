# import random
# queue = random.randint(0, 20)
queue = 5
reserve = 0
def input_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Nermuceq tiv")
			continue
		if i < 0:
			print("Nermuceq drakan tiv!")
while True:
	i = input_number("0 - exit, 1 - amragrel hert, 2 - hertum mardkanc qanaky, 3 - chexarkel herty:\n")
	if i == 0:
		print("Hajoxutyun!")
		break
	elif i == 1:
		if reserve == 0:
			queue += 1
			reserve = 1
			print("Herty hajoxutyamb amragrvel e!")
		else:
			print("Duq arden amragrveleq hertum!")
	elif i == 2:
		print("Hertum spasum en: ", queue)
	elif i == 3:
		if i > 0:
			if reserve == 1:
				queue -=1;
				reserve = 0
				print("Herty hajoxutyamb chexarkvel e!")
			else:
				print("Duq cheq amragrvel hertum!")
		else:
			print("Hertum mard chka!")