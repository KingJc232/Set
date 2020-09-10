"""
File: linkedSet.py
Developer: Jc
Goal: To Implement the Set data Structure using the Set Abstract class and a Singly Linked List 
"""

#From file import class
from set import Set
from node import Node


class LinkedSet(Set):	

	def __init__(self):
		#Pointer that will start the Singly Linked List 
		self.head = Node()

	#Adds a element to the set (ENSURE ELEMENT IS Unique) 
	def add(self, element):
		pass		

	#Private method ensure element in singly linked list unique


	#Removes a specified Element From the Set (Ensure Element Exists / not at zero )
	def remove(self, element):
		pass
	#Randomly Removes a Element From the Set (Ensure size not at zero )
	def pop(self):
		pass
	#Clears the Entire Set 
	def clear(self):
		pass

	#Ensures Object can be used with len()
	def __len__(self):
		pass

	#Ensures Object can be used with str()
	def __repr__(self):
		answer = "["
		comma = ""

		#Will itterate through the entire set 
		while self.head != None:
			answer += comma + self.head.data 
			comma = " , "
			#Go to the Next Node in the List 
			self.head = self.head.nextNode		
			
		answer += "]"	
		return answer