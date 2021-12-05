import random

def play():
	user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
	computer = random.choice(['r', 'p', 's'])
	print(f'computer: {computer}')

	while user == computer:
		print('It is a tie')
		user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
		computer = random.choice(['r', 'p', 's'])
		print(f'computer: {computer}')

	if (user=='r' and computer =='s') or (user=='p' and computer=='r') \
		or (user=='s' and computer=='p'): 
		print('User wins!')
		

	elif (computer=='r' and user =='s') or (computer=='p' and user=='r') \
		or (computer=='s' and user=='p'): 
		print('Computer wins!')
		
play()
play()