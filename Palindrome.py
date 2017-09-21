#Checking to see if a word is a Palindrome "Spelt the same in reverse"
#Author Karle Sleith

def PalindromeChecker(input):
	reversedInput = ""
	for ch in input[::-1]:
		reversedInput = reversedInput + ch
	
	if input == reversedInput:
		return print(input,"is a Palindrome")
		
	else:
		return print(input,"is a NOT Palindrome")
		
userInput = str(input("Please Input Your Word: "))
PalindromeChecker(userInput)
	