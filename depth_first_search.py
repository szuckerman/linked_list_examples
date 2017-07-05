class Node:
	def __init__(self, name, nodes=[]):
		self.name = name
		self.nodes = nodes
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