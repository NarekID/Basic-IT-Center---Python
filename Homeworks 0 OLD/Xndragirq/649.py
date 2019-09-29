while True:
	q = 0
	zIndex1 = -1
	zIndex2 = -1
	text = str(input("Mutqagreq text: "))
	for i in range(len(text)):
		if "z" in text[i]:
			q += 1
			if zIndex1 == -1:
				zIndex1 = i
			elif zIndex2 == -1:
				zIndex2 = i
			if q > 2:
				break			
	if q != 2:
		print("z qanaky havasar che 2in")
	else:
		q = zIndex2 - zIndex1
		print("Erku z mijev ka ", q - 1, " simvol") #q-1 vorpeszi zIndex2 chhashvi