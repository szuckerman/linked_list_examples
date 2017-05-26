
class Node:
	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node
	def __repr__(self):
		return "<DATA: %s>" % str(self.data)


A = Node(1)
B = Node(2)

HEAD = A
TAIL = B

A.next_node=B

C = Node(3)
D = Node(4)
E = Node(5)

def printAllNodes():
	'''This function prints all the elements of a linked list.
	We assume that the linked list is in the global environment.'''
	current_node = HEAD
	while current_node.next_node is not None:
		print(current_node)
		current_node=current_node.next_node
	print(current_node)


def returnAsPythonList(head_node):
	'''This will return the Linked List in a Python list - for testing purposes.'''
	my_list = []
	current_node = head_node
	my_list.append(current_node)
	while current_node.next_node is not None:
		current_node=current_node.next_node
		my_list.append(current_node)
	return my_list


def insertAsHead(inserted_node):
	global HEAD
	inserted_node.next_node = HEAD
	HEAD = inserted_node


# Need to fix this one, even though it prints correctly. Doesn't pass unittest.
def insertAfterHead(inserted_node):
	inserted_node.next_node = HEAD.next_node
	HEAD.next_node = inserted_node


def insertAsTail(inserted_node):
	global TAIL
	TAIL.next_node = inserted_node
	TAIL = inserted_node


def insertBeforeTail(inserted_node):
	current_node=HEAD
	while current_node.next_node is not None:
		if current_node.next_node.next_node is None:
			current_node.next_node = inserted_node
			inserted_node.next_node = TAIL
		current_node=current_node.next_node


def insertAfterNode(inserted_node, position):
	'''This function adds a node after a node of a given position.'''
	count = 1
	current_node=HEAD
	while count < position:
		current_node = current_node.next_node
		count += 1
	new_list = current_node.next_node
	current_node.next_node = inserted_node
	inserted_node.next_node = new_list


