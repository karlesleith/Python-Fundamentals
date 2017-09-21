#Merge and Sort Lists in Python
#Author Karle Sleith
def MergeLists(): 
	lOne = [1,2,3]
	lTwo = [2,3,4]

	mergedlist = lOne + lTwo
	mergedlist.sort()

	print (mergedlist)
	
MergeLists()