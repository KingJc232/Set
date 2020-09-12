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

	#Adds an element to the set (ENSURE ELEMENT IS Unique) 
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


	#Removes a specified Element From the Set 
	#If Element Doesnt Exists will return False (Failed to Remove)
	def remove(self, element):

		removedSuccessful = False #Initially False

		#Temp Iterator used to iterate through the list 
		itr = self.head
		prevItr = None #Initially Nothing

		#While the Iterator is not None
		while itr: 		
			#Element to Remove 
			if itr.data == element:
				#Removing the First Element 
				if prevItr is None: 
					self.head = self.head.nextNode #Removing the first Node
				#Removing a Mid Element or the Last Element
				else:
					prevItr.nextNode = itr.nextNode
					itr.nextNode = None #Dereferencing
				removedSuccessful = True
			prevItr = itr #Saving the Previous Node 
			itr = itr.nextNode #Go to the next Node 

		#DONT FORGET TO DECREMENT SIZE 
		if removedSuccessful:
			self._size -= 1 
		return removedSuccessful 

	#Randomly Removes an Element From the Set (Ensure size not at zero )
	def pop(self):

		#Ensures LinkedSet Not Empty 
		if self.isEmpty():
			raise Exception("Error: You Cannot Pop an Empty LinkedSet")

		#Easiest element to remove is the head so thats the one we are going to do since its a set 
		self.head = self.head.nextNode
		#Decrementing the size
		self._size -= 1


	#Clears the Entire Set 
	def clear(self):

		#While Not Empty Pop it 
		while not self.isEmpty():
			self.pop()

	#Checks if the Set is Empty or Not 
	def isEmpty(self):
		return self.size == 0 


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