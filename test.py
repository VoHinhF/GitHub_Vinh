from random import randint
print ("Nhập Bao Kéo Búa")
player = input()
computer = randint(0,2)

if computer == 0:
	computer = "Búa"
if computer == 1:
	computer = "Kéo"
if computer == 2:
	computer = "Bao"
print ("---")
print ("You choose:" + player)
print ("Computer chooses:" + computer)
print ("---")

if player == computer:
	print ("Draw")
else: 
	if player == "Kéo":
		if computer == "Búa":
			print ("Lose")
		else: 
			print ("Win")
	elif player == "Búa":
		if computer == "Bao":
			print ("Lose")
		else: 
			print ("Win")
	elif player == "Bao":
		if computer == "Kéo":
			print ("Lose")
		else: 
			print ("Win")
	else: 
		print ("Nhập sai")
