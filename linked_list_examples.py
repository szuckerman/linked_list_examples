
class Node:
	def __init__(self, data, next_node=None, previous_node=None):
		self.data = data
		self.next_node = next_node
		self.previous_node = previous_node
	def __repr__(self):
		return "<DATA: %s>" % str(self.data)


class LinkedList:
	def __init__(self, HEAD=None, TAIL=None):
		self.HEAD = HEAD
		self.TAIL = TAIL
		self._node_set = set()
		if self.HEAD is not None:
			self._node_set.add(self.HEAD)
		if self.TAIL is not None:
			self._node_set.add(self.TAIL)
		if len(self._node_set) == 2:
			self.HEAD.next_node = self.TAIL

	def add_node(func):
		def decorated_func(self, node, pos=None):
			print('%s added to set with %s function' % (node, func.__name__))
			if pos is None:
				func(self, node)
			else:
				func(self, node, pos)
			self._node_set.add(node)
		return decorated_func
	
	def printAllNodes(self):
		'''This function prints all the elements of a linked list.'''
		count = 1
		current_node = self.HEAD
		while current_node.next_node is not None:
			print('Node %s: %s' % (count, current_node))
			current_node=current_node.next_node
			count += 1
		print('Node %s: %s' % (count, current_node))
	
	def returnAsPythonList(self):
		'''This will return the Linked List as a Python list - for testing purposes.'''
		my_list = []
		current_node = self.HEAD
		my_list.append(current_node)
		while current_node.next_node is not None:
			current_node=current_node.next_node
			my_list.append(current_node)
		return my_list

	def convertToDoublyLinkedList(self):
		prior_node = self.HEAD
		current_node = prior_node.next_node
		current_node.previous_node=prior_node
		while current_node.next_node is not None:
			prior_node=current_node
			current_node=current_node.next_node
			current_node.previous_node=prior_node
	
	@add_node
	def insertAsHead(self, inserted_node):
		inserted_node.next_node = self.HEAD
		self.HEAD = inserted_node
	# Need to fix this one, even though it prints correctly. Doesn't pass unittest.
	
	@add_node
	def insertAfterHead(self, inserted_node):
		inserted_node.next_node = self.HEAD.next_node
		self.HEAD.next_node = inserted_node
	
	@add_node
	def insertAsTail(self, inserted_node):
		self.TAIL.next_node = inserted_node
		self.TAIL = inserted_node
	
	@add_node
	def insertBeforeTail(self, inserted_node):
		current_node=self.HEAD
		while current_node.next_node is not None:
			if current_node.next_node.next_node is None:
				current_node.next_node = inserted_node
				inserted_node.next_node = self.TAIL
			current_node=current_node.next_node
	
	@add_node
	def insertAfterNode(self, inserted_node, position):
		'''This function adds a node after a node of a given position.'''
		count = 1
		current_node=self.HEAD
		while count < position:
			current_node = current_node.next_node
			count += 1
		new_list = current_node.next_node
		current_node.next_node = inserted_node
		inserted_node.next_node = new_list



# Examples:
# import linked_list_examples as lle
# ll=lle.LinkedList(HEAD=lle.Node(1),TAIL=lle.Node(2))
# ll.insertBeforeTail(lle.Node(3))
# ll.insertAsHead(lle.Node(4))
# ll.printAllNodes()
# ll.insertAfterNode(lle.Node(5),3)









