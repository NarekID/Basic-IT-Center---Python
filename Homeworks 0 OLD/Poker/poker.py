import random
def input_num(message):
	while 1:
		try:
			n = int(input(message))
			return n
		except ValueError:
			print("Enter a number!")
def shuffle(array):
	n = len(array)
	for i in range(n):
		a = random.randint(0, n-1)
		b = random.randint(0, n-1)
		temp = array[a]
		array[a] = array[b]
		array[b] = temp
	return array
while 1:
	players = input_num("Enter players number (0 - exit): ")
	if players is 0:
		break
	elif players > 5:
		print("Maximum player count is 5!")
		continue
	elif players < 2:
		print("Minimum player count is 2!")
		continue
	sym = ["♥", "♦", "♠", "♣"]
	num = ["2", "3", "4", "5", "6", "7" , "8" , "9", "10" , "J", "Q" , "K", "A"]
	card = []
	for i in range(4):
		for j in range(13):
			card.append(sym[i] + num[j])
	print(card, "\n")
	card = shuffle(card)
	print(card, "\n")
	players_arr = [[0] * 2, [0] * 2, [0] * 2, [0] * 2, [0] * 2]
	j = 0
	for t in range(players):
		i = 0
		players_arr[t][i] = card[j]
		card.remove(card[j])
	for t in range(players):
		i = 1
		players_arr[t][i] = card[j]
		card.remove(card[j])

	for i in range(players):
		print("Player " + str(i+1) + " cards - ", players_arr[i])
	print(card)



	# tarberak 2 aranc .remove()



	# j = 0
	# for t in range(players):
	# 	i = 0
	# 	players_arr[t][i] = card[j]
	# 	j += 1
	# for t in range(players):
	# 	i = 1
	# 	players_arr[t][i] = card[j]
	# 	j += 1

	# for i in range(players):
	# 	print("Player " + str(i+1) + " cards - ", players_arr[i])
	# print(card)
	
	# for i in range(j, len(players_arr)):
	#	print(players_arr[i], end=" ")