from collections import deque

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


print('''
--------------------------------------------
	Starting DFS
--------------------------------------------
''')


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
dfs_tree = Tree(nodes=node_set, HEAD = A)

STACK = []
dfs_count = 1

dfs_starting_node = dfs_tree.HEAD
dfs_starting_node.number = dfs_count
dfs_count+=1



def traverse_tree(starting_node):
	global dfs_count
	for node in starting_node.nodes:
		# If node has been visited, just go to the next node in the stack
		if node.number is not None:
			continue
		# We're stacking from right to left
		STACK.append(node)
		print("Added %s" % node)
	print("Current Stack: [%s]" % ', '.join([i.name for i in STACK]))
	if STACK:
		new_node=STACK.pop()
		# Only tag nodes that haven't been visited
		if new_node.number is None:
			new_node.number=dfs_count
			dfs_count+=1
		return traverse_tree(new_node)
	else:
		print("Stack empty.  Ending recursion.")
		return

traverse_tree(dfs_starting_node)

dfs_number_dict = {node.name: node.number for node in dfs_tree.nodes}

print('''
Node Order:
''')

for k, v in sorted(dfs_number_dict.items()):
	print("Node %s: %s" % (k, v))


print('''
--------------------------------------------
	Starting BFS
--------------------------------------------
''')

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
bfs_tree = Tree(nodes=node_set, HEAD = A)

QUEUE = deque([])
bfs_count = 1

bfs_starting_node = bfs_tree.HEAD
bfs_starting_node.number = bfs_count
bfs_count+=1


def traverse_tree_bfs(starting_node):
	global bfs_count
	for node in starting_node.nodes:
		# If node has been visited, just go to the next node in the stack
		if node.number is not None:
			continue
		# We're stacking from right to left
		QUEUE.append(node)
		print("Added %s" % node)
	print("Current Queue: [%s]" % ', '.join([i.name for i in QUEUE]))
	if QUEUE:
		new_node=QUEUE.popleft()
		# Only tag nodes that haven't been visited
		if new_node.number is None:
			new_node.number=bfs_count
			bfs_count+=1
		return traverse_tree_bfs(new_node)
	else:
		print("Queue empty.  Ending recursion.")
		return

traverse_tree_bfs(bfs_starting_node)

bfs_number_dict = {node.name: node.number for node in bfs_tree.nodes}

print('''
Node Order:
''')

for k, v in sorted(bfs_number_dict.items()):
	print("Node %s: %s" % (k, v))

