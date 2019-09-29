while True:
	q = 0
	xIndex = 0
	text = str(input("Mutqagreq text: "))
	for i in range(len(text)):
		if "x" in text[i]:
			q += 1
			xIndex = i
		if q > 1:
			print("x qanaky 1ic avel e")
			break
	if q > 1:
		continue
	q = 0
	for i in range(xIndex, len(text)):
		if "0" in text[i]:
			q += 1
	print("0 neri qanaky textum = ", q)