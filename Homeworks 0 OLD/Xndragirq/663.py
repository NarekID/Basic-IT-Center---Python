while True:
	text = str(input("Mutqagreq text: "))
	gumar = 0
	q = 0
	for i in range(len(text)):
		if "c" in text[i]:
			gumar += i
			q += 1
	if q == 0:
		print("c tary bacakayum e!")
	else:
		print("mijin tvabanakany = ", gumar, " / ", q , " = ", gumar/q)