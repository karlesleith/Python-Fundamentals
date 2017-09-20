#Guessing Game

import random
from random import randint

guesses = 3;
randomNumber = randint(1,10)
win = False; 

while guesses > 0 :
	print("\nNumber of Guesses Left: "+ str(guesses))
	guess = int(input("Pick and number between 1 - 10 :\n"))
	
	if guess > randomNumber:
		print("Your number was too High")
		guesses = guesses-1;

	elif guess < randomNumber:
		print("Your number was too Low")
		guesses = guesses -1;
	
	elif guess == randomNumber:
		print("\nYou Win!")
		break
		
print("\nGame Over The Number was "+ str(randomNumber))
	

		




