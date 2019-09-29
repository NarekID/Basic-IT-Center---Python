while True:
	text = str(input("Mutqagreq text: "))
	text2 = ""
	vIndex = -1
	for i in range(len(text)):
		if "v" in text[i]:
			vIndex = i;
			break;
	if vIndex == -1:
		print("v tary bacakayum e!")
		continue
	for i in range(vIndex + 1): #vorpeszi tpi v
		text2 += text[i]
	print(text2)