import unittest
import linked_list_examples as lle
from copy import copy

class LinkedListTests(unittest.TestCase):
	'''Tests for the various methods to adjust linked lists.'''

	def setUp(self):
		"""Create a linked list to use"""
		self.ll = lle.LinkedList(HEAD=lle.Node(1), TAIL=lle.Node(2))
		self.node_3 = lle.Node(3)


	def tearDown(self):
		pass


	def test_insert_as_head(self):
		previous_head = copy(self.ll.HEAD)
		self.ll.insertAsHead(self.node_3)
		self.assertEqual(self.node_3.next_node.data, previous_head.data)


	def test_insert_after_head(self):
		previous_node = copy(self.ll.HEAD)
		self.ll.insertAfterHead(self.node_3)
		self.assertEqual(self.node_3.next_node.data, previous_node.next_node.data)


if __name__ == '__main__':
	unittest.main()