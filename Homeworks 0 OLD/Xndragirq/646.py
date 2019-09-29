while True:
	q = 0
	text = str(input("Mutqagreq text: "))
	for i in range(len(text)):
		if "a" in text[i]:
			q += 1
	print(q)