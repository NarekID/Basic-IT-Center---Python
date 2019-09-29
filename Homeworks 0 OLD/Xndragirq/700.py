while True:
	text1 = str(input("Mutqagreq arajin text: "))
	text2 = str(input("Mutqagreq erkrord text: "))
	while len(text2) > len(text1):	 	
		print("Erkrord texty petq e arajinic karch lini!")
		text2 = str(input("Mutqagreq erkrord text: "))
	text1 = text1.split(text2)
	print(text1)
	print("Erkror texty krknvum e ",len(text1)-1," angam.") #verjin elementy vorpeszi chhashvi