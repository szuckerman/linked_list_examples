import unittest
import linked_list_examples as lle

class LinkedListTests(unittest.TestCase):
	'''Tests for the various methods to adjust linked lists.'''

	def setUp(self):
		"""Create a linked list to use"""
		self.A = lle.Node(1)
		self.B = lle.Node(2)

		self.HEAD = self.A
		self.TAIL = self.B

		self.A.next_node=self.B

		self.C = lle.Node(3)
		self.D = lle.Node(4)
		self.E = lle.Node(5)


	def tearDown(self):
		pass


	def test_insert_as_head(self):
		lle.insertAsHead(self.C)
		self.assertEqual(self.C.next_node.data, self.HEAD.data)


	def test_insert_after_head(self):
		lle.insertAfterHead(self.C)
		self.assertEqual(self.C.next_node.data, self.HEAD.next_node.data)


if __name__ == '__main__':
	unittest.main()
