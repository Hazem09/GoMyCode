import random

number = random.randint(1,100)

should_continue = True 
while should_continue:
	guess = int(input("enter your guess"))
	if number < guess:
		print("too high, try again")
	elif number > guess:
		print("too low, guess again")
	else:
		should_continue = False
		print('congrats you won')
