import random

def guess(x):

	random_number=random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		print(guess)
		if guess < random_number:
			print('Sorry, guess again. Too low:(')
		elif guess > random_number:
			print('Sorry, guess again. Too high:(')
	
	print(f'Congrats! You have guessed the number. It was {random_number}')


def computer_guess(x):

	secret_number=int(input('Choose a number for the computer to guess:'))

	random_number2=random.randint(1,x)
	print(random_number2)

	while random_number2 != secret_number:
		random_number2=random.randint(1,x)
		print(random_number2)

	if random_number2==secret_number:
		print('Congratulations computer, you have guessed the number!')


computer_guess(10)