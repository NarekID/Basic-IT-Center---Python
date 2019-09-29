while True:
	q = 0
	text = str(input("Mutqagreq text: "))
	text2 = str(input("Mutqagreq 2rd text: "))
	while len(text) != len(text2):
		print("2rd texti nisheri qanaky havasar che 1in texti nisheri qanakin(",len(text),"), porceq krkin!")
		text2 = str(input("Mutqagreq 2rd text: "))
	for i in range(len(text)):
		for j in range(len(text2)):
			if text[i] in text2[j]:
				q += 1
				break
	print("Havasar nisheri qanaky = ",q) #q-1 vorpeszi zIndex2 chhashvi