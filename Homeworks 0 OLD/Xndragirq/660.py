while True:
	text = str(input("Mutqagreq text: "))
	text2 = list(text)
	for i in range(0,len(text2),3):
		text2[i] = "a"
	print("".join(text2))