while True:
	text = str(input("Mutqagreq text: "))
	q = 0
	if "x" in text:
		for i in range(len(text)):
			if "c" in text[i]:
				q += 1
		print("c qanaky = ", q)
	else:
		for i in range(len(text)):
			if "d" in text[i]:
				q += 1
		print("d qanaky = ", q)