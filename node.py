"""
File: node.py
Developer: Jc
Goal: To Define a Node Class to be used in LinkedSet
"""


#Singly Link List
class Node:

	def __init__(self, data = None, nextNode = None):
		self._data = data

		self._nextNode = nextNode

	@property
	def nextNode(self):
		return self._nextNode
	

	#Defining a Setter for the nextNode Property	
	@nextNode.setter
	def nextNode(self, nextNode):
		self._nextNode = nextNode


	def __eq__(self, other):
		return isinstance(other, Node) and self.data == other.data

	def __ne__(self, other):
		return isinstance(other, Node) and self.data != other.data
