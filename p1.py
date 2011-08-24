# class for entries in array TREE
# @instance lc		left child of the tree
# @instance rc		right child of the tree
# @instance parent	parent of the tree (None if root)
class t :
	def __init__(self, lc=None, rc=None, parent=None) :
		self.lc = lc
		self.rc = rc
		self.parent = parent
	def __str__(self) :
		return str(self.lc) + "\t" + str(self.rc) + "\t" + str(self.parent)

# class for ALPHABET entries
# @instance symb	symbol for this entry
# @instance prob	probability of this entry appearing
# @instance leaf	the leaf associated with this entry
class a :
	def __init__(self, symb, prob, leaf) :
		self.symb = symb
		self.prob = prob
		self.leaf = leaf
	def __str__(self) :
		return str(self.symb) + "\t" + str(self.prob) + "\t" + str(self.leaf)
		
# class for FOREST elementes
# @instance weight	weight of this entry
# @instance root	index of entry in TREE containing this element's root
class f :
	def __init__(self, weight, root) :
		self.weight = weight
		self.root = root
	def __str__(self) :
		return str(self.weight) + "\t" + str(self.root)

# sets least and second to the indices in FOREST of the trees of smallest weight.  We assume global LASTTREE >= 1.
# @param least		destination of index of smallest weight in FOREST
# @param second		destination of index of second smallest weight in FOREST
# inspired by procedure "lightones", Fig 3.27 (p.100)
def lightones(least, second) :
	# initialize least and second, considering first two trees
	if FOREST[0].weight <= FOREST[1].weight :
		least = 0
		second = 1
	else :
		least = 1
		second = 0
	# now let i run from 3 to global LASTTREE.  At each iteration least is the tree of smallest weight among the first i trees in FOREST, and second is the next smallest of these
	for k in range(2, len(FOREST)) :
		if FOREST[k].weight < FOREST[least].weight :
			second = least
			least = k
		elif FOREST[k].weight < FOREST[second].weight :
			second = k
	return [least, second]

#returns new node whose left and right children are FOREST[lefttree].root and FOREST[righttree].root.
# @param lefttree	node that will be the new left node
# @param righttree	node that will be the new right node
# @return 		node with children lefttree and righttree
def create(lefttree, righttree, lastnode) :
	lastnode = lastnode + 1
	
	print "l, r, last:", lefttree, righttree, lastnode
	
	# cell for new node is TREE[LASTNODE]
	TREE[lastnode].lc = FOREST[lefttree].root
	TREE[lastnode].rc = FOREST[righttree].root

	# now enter parent pointers for new node and its children
	TREE[lastnode].parent = None
	TREE[FOREST[lefttree].root].parent = lastnode
	TREE[FOREST[righttree].root].parent = lastnode
	return lastnode
	
	
def Huffman() :
	i = 0
	j = 0
	lastnode = 0
	while len(FOREST) > 1 :
		ij = lightones(i, j)
		i = ij[0]
		j = ij[1]
		print "i, j:", i, j, "\n"
		newroot = create(i, j, lastnode)
		lastnode = newroot

		# now replace tree i by the tree whose root is newroot
		FOREST[i].weight = FOREST[i].weight + FOREST[j].weight
		FOREST[i].root = newroot

		# next, replace tree j, which is no longer needed, by global LASTTREE, and shrink FOREST by one
		FOREST[j] = FOREST[-1]
		del FOREST[-1]
	return	
	
# FOREST array initialization
# data from problem 3.20 (p.106), scaled to 0-100 instead of 0-1 to avoid issues with Python's floating point type
# structure from Fig 3.25 (p.99)
#   _________
#0 |  07 | 0 |
#1 |  09 | 1 |
#2 |  12 | 2 |
#3 |  22 | 3 |
#4 |  23 | 4 |
#5 |  27 | 5 |
#  +-----+---+
#  WEIGHT ROOT

FOREST = [f(7,0), f(9,1), f(12,2), f(22,3), f(22,4), f(27,5)]

# ALPHABET array initialization
# data from problem 3.20 (p.106), scaled to 0-100 instead of 0-1 to avoid issues with Python's floating point type
# structure from Fig 3.25 (p.99)
#   _____________
#0 | a |  07 | 0 |
#1 | b |  09 | 1 |
#2 | c |  12 | 2 |
#3 | d |  22 | 3 |
#4 | e |  23 | 4 |
#5 | f |  27 | 5 |
#  +---+-----+---+
#  SYM |PROB |LEAF

ALPHABET = [a('a',7,0), a('b',9,1), a('c',12,2), a('d',22,3), a('e',23,4), a('f',27,5)]

# TREE array initialization
# data from problem 3.20 (p.106), scaled to 0-100 instead of 0-1 to avoid issues with Python's floating point type
# structure from Fig 3.25 (p.99)
#   ___________
#0 | 0 | 0 | 0 |
#1 | 0 | 0 | 0 |
#2 | 0 | 0 | 0 |
#3 | 0 | 0 | 0 |
#4 | 0 | 0 | 0 |
#5 | 0 | 0 | 0 |
#  +---+---+---+
#   LC  RC  PARENT

# extra three locations required as padding for output
n = None
TREE = [t(n,n,n), t(n,n,n), t(n,n,n), t(n,n,n), t(n,n,n), t(n,n,n), t(n,n,n), t(n,n,n)]

print "----- Initial values -----"
print "FOREST:"
for k in range(len(FOREST)):
	print FOREST[k]
print

print "ALPHABET:"
for k in range(len(ALPHABET)):
	print ALPHABET[k]
print

print "TREE:"
for k in range(len(TREE)):
	print TREE[k]
print


Huffman()
print "----- Final values -----"
print "FOREST:"
for k in range(len(FOREST)):
	print FOREST[k]
print

print "ALPHABET:"
for k in range(len(ALPHABET)):
	print ALPHABET[k]
print

print "TREE:"
for k in range(len(TREE)):
	print TREE[k]
print