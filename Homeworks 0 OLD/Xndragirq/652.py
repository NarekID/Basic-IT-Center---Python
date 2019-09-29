while True:
	text3 = ""
	k = 0
	text = str(input("Mutqagreq text: "))
	text2 = str(input("Mutqagreq 2rd text: "))
	while len(text) != len(text2):
		print("2rd texti nisheri qanaky havasar che 1in texti nisheri qanakin(",len(text),"), porceq krkin!")
		text2 = str(input("Mutqagreq 2rd text: "))
	for j in range(len(text2)):
		for i in range(len(text)):
			if text2[j] in text[i]:
				text3 += text2[j]
				break
	print(text3)