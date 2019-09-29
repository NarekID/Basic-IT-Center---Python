while True:
	text = str(input("Mutqagreq text: "))
	i = 0
	l = len(text) - 1
	while True:
		if text[i] in text[l]:
			i += 1
			l -= 1
			equal = True
			if i == l or i + 1 == l: #michev kesy gna, 2rd angam nuyn texov chancni
				break
		else:
			equal = False
			break
	print(equal)