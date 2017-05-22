# Linked Lists in Python

class Node:
	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node
	def __repr__(self):
		return("<DATA: %s>" % str(self.data))


A = Node(1)
B = Node(2)

HEAD = A
TAIL = B

A.next_node=B

C = Node(3)


# Print all elements
def printAllNode():
	current_node = HEAD
	while current_node.next_node is not None:
		print(current_node)
		current_node=current_node.next_node
	print(current_node)


# Insert an element

	## As the HEAD
temp_node = HEAD
HEAD = C
HEAD.next_node = temp_node

	## after the HEAD
temp_node = HEAD.next_node
HEAD.next_node = C
HEAD.next_node.next_node = temp_node


	## as the tail
TAIL.next_node = C

	## before the tail
	## in the middle somewhere








