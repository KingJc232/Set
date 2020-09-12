"""
File: main.py
Developer: Jc
Goal: To Test the custom Set Data Structure 
Note: Trying to Use OOP Design 
"""


from linkedSet import LinkedSet



def main():

	linkedSet = LinkedSet()

	linkedSet.add(1)
	linkedSet.add(2)
	linkedSet.add(3)
	linkedSet.add(4)



	print("Before Removal: %s" % linkedSet)
	print("Size: %d" % len(linkedSet))


	print("After Removal: %s" % linkedSet)
	print("Size: %d" % len(linkedSet))


if __name__ == "__main__":
	main() 