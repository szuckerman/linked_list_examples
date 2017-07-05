class Node:
	def __init__(self, name, nodes=[], number=None):
		self.name = name
		self.nodes = nodes
		self.number = number
	def __repr__(self):
		return "<Node %s>" % self.name

class Tree:
	def __init__(self, nodes=set(), HEAD=None):
		self.nodes = nodes
		self.HEAD = HEAD

# Tree from the pluralsight.com Algorithmics Course used as an example

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')

A.nodes = [B, C]
B.nodes = [D, E]
C.nodes = [E, F]
D.nodes = [G]
E.nodes = []
F.nodes = [G, H, I]
G.nodes = [D, E]
H.nodes = []
I.nodes = []

node_set = {A, B, C, D, E, F, G, H, I}
my_tree = Tree(nodes=node_set, HEAD = A)


STACK = []
count = 1

starting_node = my_tree.HEAD
starting_node.number = count
count+=1


def traverse_tree(starting_node):
	global count
	for node in starting_node.nodes:
		if node.number is not None:
			continue
		# We're stacking from right to left
		STACK.append(node)
		print("Added %s" % node)
	print("Current Stack: [%s]" % ', '.join([i.name for i in STACK]))
	if STACK:
		new_node=STACK.pop()
		if new_node.number is None:
			new_node.number=count
			count+=1
		return traverse_tree(new_node)
	else:
		print("Stack empty.  Ending recursion.")
		return

traverse_tree(starting_node)

number_dict = {node.name: node.number for node in my_tree.nodes}

for k, v in sorted(number_dict.items()):
	print("Node %s: %s" % (k, v))

