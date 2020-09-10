"""
File: set.py
Developer: Jc
Goal: To Define a Set Data Structure 
Notes: Remember a Set is a unordered data structure that holds unique elemetns 
"""


#Used this as the interface to the LinkedSet
class Set:

	def __init__(self):
		pass

	#Abstract: Adds a element to the set 
	def add(self, element):
		raise NotImplementedError("Please Implement Add Method")

	#Abstract: Removes a specified Element From the Set 
	def remove(self, element):
		raise NotImplementedError("Please Implement Remove Method")

	#Abstract: Randomly Removes a Element From the Set
	def pop(self):
		raise NotImplementedError("Please Implement Pop Method")

	#Abstract: Clears the Entire Set 
	def clear(self):
		raise NotImplementedError("Please Implement Clear Method")
