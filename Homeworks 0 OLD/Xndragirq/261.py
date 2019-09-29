def input_number(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq tiv!")
while True:
	n = input_number("Mutqagreq zangvaci erkarutyuny (0 - elq cragric): ")
	while n < 0:
		print("Mutqagreq drakan tiv!")
		n = input_number("Mutqagreq zangvaci erkarutyuny (0 - elq cragric): ")
	if n is 0:
		print("Hajoxutyun!")
		break
	arrX = [0] * n
	arrY = [0] * n
	summ = 0
	summ2 = 0
	count = 0
	count2 = 0
	for i in range(n):
		arrX[i] = input_number("ArrX["+str(i)+"] = ")
		while type(arrX[i]) is not int:
			arrX[i] = input_number("ArrX["+str(i)+"] = ")
		summ += arrX[i]
		count += 1
	print("")
	for i in range(n):
		arrY[i] = input_number("ArrY["+str(i)+"] = ")
		while type(arrY[i]) is not int:
			arrY[i] = input_number("ArrY["+str(i)+"] = ")
		summ2 += arrY[i]
		count2 += 1

	print("ArrX mijin tvabanakan = " , summ/count, "\nArrY mijin tvabanakan =", summ2/count2, "\nArtadryaly = ",(summ/count) * (summ2/count2)) 