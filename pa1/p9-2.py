# Leftmost Child/Right Sibling implementation of Trees

# Node class - each object of class node is a node a tree
# @param label 	label of the node (1, 2, 3, ...)
# @param lc 	left child of the node
# @param rs 	right sibling of the node
# @param parent	the node's parent
class node :
	# constructor
	def __init__(self) :
		self.label = None
		self.lc = None
		self.rs = None
		self.parent = None
	
	# for easier printing
	def __str__(self):
                return str(self.label)

# Tree class
# @param cellspace	list of objects of type node
# @param end		integer representation of one-past-last *used* object in list
# @param root		the root node of the tree.
class tree :

	# constructor.  Creates only null trees.
	def __init__(self) :
		self.cellspace = None
		self.root = None

# returns a null (empty) tree.
def MAKENULL() :
	temp = tree()
	temp.cellspace = [None]*MAXNODES
	return temp

# returns the parent of a node
# @param n	node in question
def PARENT(n, T) : 
	return T.cellspace[n.parent]

# returns the leftmost child of a node
# @param n 	node in question
def LEFTMOST_CHILD(n, T) :
	if n.lc is None :
		return None
	else :
		return T.cellspace[n.lc]
	print n, "does not exist in the tree."

# returns the right sibling of a node
# @param n 	node in question
def RIGHT_SIBLING(n, T):
	if n.rs is None :
		return None
	else :
		return T.cellspace[n.rs]
	print n, "does not exist in the tree."
		
# returns the label of a node
# @param n 	node in question
def LABEL(n) :
	return n.label

# returns a tree with root/leaf node v.  ...that's it.
# @param v	label of the root/leaf node
def CREATE0(v) :
	# make new, empty tree
	temp = MAKENULL()

	#set root's values
	temp.cellspace[v] = node()
	temp.cellspace[v].label = v
	
	# root is v
	temp.root = v
	return temp
	
# returns a tree with root node labeled v and child subtree T
# @param v	label of the new root node (it better be an integer, or things will break badly)
# @param T	subtree to the be leftmost (er... only) chlid of the new root
def CREATE1(v, T) :
	# make new, empty tree
	temp = MAKENULL()
	
	# copy T's cellspace
	for i in range(0, MAXNODES) :
		if T.cellspace[i] is not None :
			temp.cellspace[i] = T.cellspace[i]
	# set new root
	temp.cellspace[v] = node()
	temp.cellspace[T.root] = node()

	# set root's values
	temp.cellspace[v].label = v
	temp.cellspace[v].lc = T.root
	temp.rs = None	# not needed, but good for explicitacity.
	
	# set T's values
	temp.cellspace[T.root].label = T.root
	temp.cellspace[T.root].rs = None	# explicit
	temp.cellspace[T.root].parent = v
	
	# root is v
	temp.root = v

	return temp

# returns a tree with root node labeled v and children subtrees T1 and T2
# @param v	label of the new root node (it better be an integer, or things will break badly)
# @param T1	subtree to be the leftmost child of the new root
# @param T2	subtree to be the rightmost child of the new root
def CREATE2(v, T1, T2) :
	# make new, empty tree
	temp = MAKENULL()

	# copy T1's cellspace
	#temp.cellspace = T1.cellspace
	# merge in T2's cellspace
	for i in range(0, MAXNODES) :
		if T1.cellspace[i] is not None :
			temp.cellspace[i] = T1.cellspace[i]
		elif T2.cellspace[i] is not None :
			temp.cellspace[i] = T2.cellspace[i]
			
	# set new roots
	temp.cellspace[v] = node()
	temp.cellspace[T1.root] = node()
	temp.cellspace[T2.root] = node()
	
	# set root's values
	temp.cellspace[v].label = v
	temp.cellspace[v].lc = T1.root
	temp.cellspace[v].rs = None	# being explicit
	
	# set T1's cell's attributes
	temp.cellspace[T1.root] = T1.cellspace[T1.root]
	temp.cellspace[T1.root].rs = T2.root
	temp.cellspace[T1.root].parent = v

	# set T2's cell's attributes
	temp.cellspace[T2.root] = T2.cellspace[T2.root]
	temp.cellspace[T2.root].rs = None
	temp.cellspace[T2.root].parent = v
	
	# root is v
	temp.root = v

	return temp
	
# returns a tree with root node labeled v and children subtrees T1, T2, and T3
# @param v	label of the new root node (it better be an integer, or things will break badly)
# @param T1	subtree to be the leftmost child of the new root
# @param T2	subtree to be to the right of T1
# @param T3	subtree to be to the right of T2
def CREATE3(v, T1, T2, T3) :
	# make new, empty tree
	temp = MAKENULL()
	
	for i in range(0, MAXNODES) :
		if T1.cellspace[i] is not None :
			temp.cellspace[i] = T1.cellspace[i]
		elif T2.cellspace[i] is not None :
			temp.cellspace[i] = T2.cellspace[i]
		elif T3.cellspace[i] is not None :
			temp.cellspace[i] = T3.cellspace[i]
	
	# set new roots
	temp.cellspace[v] = node()
	temp.cellspace[T1.root] = node()
	temp.cellspace[T2.root] = node()
	temp.cellspace[T3.root] = node()
	
	# set root's values
	temp.cellspace[v].label = v
	temp.cellspace[v].lc = T1.root
	temp.cellspace[v].rs = None	# being explicit
	
	# set T1's cell's attributes
	temp.cellspace[T1.root] = T1.cellspace[T1.root]
	temp.cellspace[T1.root].rs = T2.root
	temp.cellspace[T1.root].parent = v

	# set T2's cell's attributes
	temp.cellspace[T2.root] = T2.cellspace[T2.root]
	temp.cellspace[T2.root].rs = T3.root
	temp.cellspace[T2.root].parent = v
	
	# set T3's cell's attributes
	temp.cellspace[T3.root] = T3.cellspace[T3.root]
	temp.cellspace[T3.root].rs = None
	temp.cellspace[T3.root].parent = v
	
	# root is v
	temp.root = v

	return temp




# returns the root of tree T
# @param T	the tree in question
def ROOT(T) :
	return T.cellspace[T.root]

# prints contents of tree t containing root r [inorder].  There is probably a
# 	way to put this in tree class's __str__ function, I just haven't done it yet.
# 	String concatentation, most likely.
# @param r	the root of the tree in question
def printTree(n, T) :
	if n.lc is None :
		print n,
	else :
		printTree(T.cellspace[n.lc], T)
		print n,
		tmp = LEFTMOST_CHILD(n,T)
		tmp = RIGHT_SIBLING(tmp, T)
		while tmp is not None :
			printTree(tmp, T)
			tmp = RIGHT_SIBLING(tmp, T)

#########################################################

# returns the height of a node in a tree
# @param n	node in question
# @param T	tree containing n
def height(n, T, m, i) :
	if LEFTMOST_CHILD(n, T) is None :
		return i+1		# no idea why this must be different than p9-2.py :)
	else :
		tmp = LEFTMOST_CHILD(n, T)
		# for each other sibling, makelevels
		while tmp is not None :
			v = height(tmp, T, m, i+1)
			if v > m :
				m = v
			tmp = RIGHT_SIBLING(tmp, T)
		if i > m :
			m = i
		return m

MAXNODES = 100

#### A..N replaced by integers 1..14 for simplicity.
M = CREATE0(13)
N = CREATE0(14)
I = CREATE2(9, M, N)

D = CREATE0(4)
E = CREATE1(5, I)

F = CREATE0(6)

J = CREATE0(10)
K = CREATE0(11)
G = CREATE2(7, J, K)

L = CREATE0(12)
H = CREATE1(8, L)

B = CREATE2(2, D, E)

F = CREATE0(6)
C = CREATE3(3, F, G, H)

A = CREATE2(1, B, C)

max = 0
h = height(ROOT(A), A, max, 0)
print "height of tree: ",h
