#Fizzbuzz Problem in Python
#Author Karle Sleith

import math

for n in list(range(0,101)):
	word = ""
	if(n % 3 == 0): # if i is divisable by 3
		word += 'Fizz'
	if(n % 5 == 0):# if i is divisable by 5
		word += 'Buzz'
	if(word == ""):
		word += str(i)

	print(word)
		
print('\n Do Do Doooo, GoodBye!')
