def checkIn(mylist, searchItem):
	"""
	Function to iterate through the collection of letters
	Find the given letter in terms of its position in the collection
	"""
	
	if searchItem in mylist:								# Checks if letter is in the collection
		return mylist.index(searchItem)		   # returns the position of the letter in the list
		
	else:
		return "{} is not im the collection of letters".format(searchItem)   
		
collection = ['me', 2, 6, 8, 9]
x = 'me'
print(checkIn(collection, x))