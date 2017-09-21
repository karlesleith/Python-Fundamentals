#Function for Reving a Sting in Python 3 
#Author Karle Sleith 


def ReverseString(s):

	reverseInput = s[::-1]
	
	return print("\n",reverseInput)
   
		
userInput = str(input("Please Input Your Word: "))
ReverseString(userInput)