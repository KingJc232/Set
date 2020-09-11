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
		self.head = None 
		self._size = 0 #Initially Zero Keeps track of the size of the Set 

	@property
	def size(self):
		return self._size

	#Adds a element to the set (ENSURE ELEMENT IS Unique) 
	def add(self, element):

		#Ensuring the Element is not in the set 
		if self._foundDuplicate(element) == False:
			#Add the element to the list 
			tempNode = Node(element)

			#Empty Set 
			if self._size == 0: 
				self.head = tempNode
			#More than one element in the Set 
			else:
				tempNode.nextNode = self.head #Linking the Nodes 
				self.head = tempNode #Updating the Head

			self._size += 1 #Incrementing the size of the data structure 
			return True


		#Else return false since you didnt add it 
		return False

	#Private method ensure element in singly linked list unique
	def _foundDuplicate(self, element):

		#Have to Itterate the entire Singly Linked list

		#Creating a Temp Node Iterater 
		temp = self.head
		found = False #Initially have not found the element in the Linked List 

		while temp is not None and found == False:

			if temp.data == element:
				found = True #Found The Element Break 
				break
			else:
				temp = temp.nextNode # Go to the next node in the chain 

		return found

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
		return self.size

	#Ensures Object can be used with str()
	def __repr__(self):
		#Iterator
		temp = self.head
		answer = "["
		comma = ""

		#Will itterate through the entire set 
		while temp is not None:

			answer += comma + str(temp.data) 
			comma = " , "
			#Go to the Next Node in the List 
			temp = temp.nextNode		
			
		answer += "]"	
		return answer