from timeit import Timer

class Node:
	def __init__(self):
		self.cargo = None
		self.nxt = None
	
	def __str__(self):
		return str(self.cargo) 	

class myList:
	def __init__(self):
		self.head = None
		self.cur = None

# clear list
#def MAKENULL() :
#	temp = myList()
#	
#	return temp

# return head of list
def FIRST(lst) :
	return lst.head

# return last node in list
def END(lst) :
	# if empty
	if lst.head is None and lst.cur is None:
		return None
	else :
		temp = lst.head
		while temp.nxt:	# may need change to while temp.nxt
			temp = temp.nxt
		return temp

# find position of a specific value in the list
def LOCATE(val, lst) :
	count = 0
	temp = FIRST(lst)
	while temp :
		if temp.cargo == val :
			return count
		else :
			count += 1
			temp = temp.nxt;
	return -1

# get data at specific position in list
def RETREIVE(pos, lst) :
	temp = FIRST(lst)
	for k in range(0, pos) :
		if temp.nxt != None :
			temp = temp.nxt
	return temp

# get next position in list
def NEXT(n) :
	return n.nxt
	

# get previous position from node
def PREVIOUS(lst) :
	temp = FIRST(lst)
	while temp :
		if temp.nxt == lst.cur :
			return temp
		else :
			temp = temp.nxt
	return None # no change if doesn't exist
	
# head insertion, returns new head
def INSERT(val, pos, lst) :
	# create new node with cargo 'val'
	n = Node()
	# set it's 'cargo' field to the 'val' parameter
	n.cargo = val
	if pos is None :
		n.nxt = None
		lst.head = n
		lst.cur = lst.head
		return
	elif (pos == FIRST(lst) and FIRST(lst) != END(lst)) or (pos == 0):
		# set n's 'nxt' field to the current list header
		n.nxt = lst.head
		# change the current header to the newly created node
		lst.head = n
		# change the current position to the new list head
		lst.cur = lst.head
		return
	else :
		if lst.head is None :
			lst.head = n
			lst.cur = n
		else :
			# copy lst
			tmp = FIRST(lst)
			while tmp and pos > 1 :
				tmp = tmp.nxt
				pos -= 1
			n.nxt = tmp.nxt
			tmp.nxt = n
			# copy tmp into lst
			#lst = tmp 	        
		return

def DELETE(pos, lst) :
	temp = FIRST(lst)
	# move to just before pos
	if pos == 0 :
		lst.head = temp.nxt
	elif pos == END(lst) :
		if temp.nxt == None :
			lst = MAKENULL()
		else :
			while (temp.nxt).nxt :
				temp = temp.nxt
			temp.nxt = None
	else :
		while pos - 1 > 0 :
			temp = temp.nxt
			pos -= 1
		first = temp
		second = temp.nxt
		first.nxt = second.nxt
	lst.cur = lst.head

def printList(lst) :
	temp = FIRST(lst)
	if temp is None :
		print "empty",
	else :
		while temp :
			print temp,
			temp = temp.nxt
	print
	
################################################################################

class tree:
	def __init__(self):
		self.cellspace = None
		self.root = None

# return a node's leftmost child, or None if it is an end node
# @param n	node in question
# @param T	source tree containing n
def LEFTMOST_CHILD(n, T) :
	# any node's leftmost child is the first element pointed to by the node
	for i in range(len(T.cellspace)) :
		if T.cellspace[i] is not None :
			if LABEL( FIRST(T.cellspace[i]) ) == LABEL(n) :
				return NEXT(FIRST(T.cellspace[i]))
	return None

# return a node's parent, or None if it is the root
# @param n	node in question
# @param T	source tree containing n
def PARENT(n, T) :
	if n == T.cellspace[T.root] :
		return None
	else :
		# parse through cellspace, test if each element contains n
		for i in range(0, len(T.cellspace)) :
			if T.cellspace[i] is not None :
				p = LOCATE(n.cargo, T.cellspace[i])
				if p != -1 and p!=0:
					return FIRST(T.cellspace[i])
		return None
			
# returns the right sibling of a node, 
# None if it is the rightmost node,
# or None if the value isn't found
# @param n	node in question
# @param T	source tree containing n
def RIGHT_SIBLING(n, T) :
	for i in range(0, len(T.cellspace)) :
		if T.cellspace[i] is not None :
			p = LOCATE(n.cargo, T.cellspace[i])
			if p != -1 and p != 0:
				return NEXT(RETREIVE(p, T.cellspace[i]))
	return None
					
# returns root node of a tree
# @param T	tree in question
def ROOT(T) :
	return FIRST(T.cellspace[T.root])

# creates and returns an empty tree
def MAKENULL() :
	temp = tree()
	temp.cellspace=[None]*MAXNODES

	return temp

# gets data at a node
# @param n	node in question
def LABEL(n) :
	return n.cargo

# returns a tree with root/leaf node v.  ...that's it.
# @param v      label of the root/leaf node
def CREATE0(v) :
	# create null tree
	n = MAKENULL()
	# initialize tree as a list
	n.cellspace[v] = myList()
	n.root = v
	# insert v into the list
	INSERT(v, END(n.cellspace[v]), n.cellspace[v])
	return n
	
# returns a tree with root node labeled v and children subtree T
# @param v      label of the new root node (it better be an integer, or things will break badly)
# @param T     subtree to be the leftmost child of the new root
def CREATE1(v, T) :
	n = MAKENULL()
	for i in range(0, len(T.cellspace)) :
		if T.cellspace[i] is not None :
			n.cellspace[i] = T.cellspace[i]
	n.cellspace[v] = myList()
	n.root = v

	# child insertions
	INSERT(v, END(n.cellspace[v]), n.cellspace[v])
	INSERT(T.root, END(n.cellspace[v]), n.cellspace[v])

	return n
	
# returns a tree with root node labeled v and children subtrees T1 and T2
# @param v      label of the new root node (it better be an integer, or things will break badly)
# @param T1     subtree to be the leftmost child of the new root
# @param T2     subtree to be the rightmost child of the new root
def CREATE2(v, T1, T2) :
	n = MAKENULL()

	# copy T1 and T2's cellspaces into n's
	for i in range(0, len(T1.cellspace)) :
		if T1.cellspace[i] is not None :
			n.cellspace[i] = T1.cellspace[i]
		elif T2.cellspace[i] is not None :
			n.cellspace[i] = T2.cellspace[i]
	n.cellspace[v] = myList()
	n.root = v

	# insertions
	INSERT(v, END(n.cellspace[v]), n.cellspace[v])
	INSERT(T2.root, END(n.cellspace[v]), n.cellspace[v])
	INSERT(T1.root, END(n.cellspace[v]), n.cellspace[v])

	return n
	
# returns a tree with root node labeled v and children subtrees T1, T2, and T3
# @param v      label of the new root node (it better be an integer, or things will break badly)
# @param T1     subtree to be the leftmost child of the new root
# @param T2     subtree to be to the right of T1
# @param T3     subtree to be to the right of T2
def CREATE3(v, T1, T2, T3) :
	n = MAKENULL()
	
	# copy T1, T2, and T3's cellspaces into n's
	for i in range(0, len(T1.cellspace)) :
		if T1.cellspace[i] is not None :
			n.cellspace[i] = T1.cellspace[i]
		elif T2.cellspace[i] is not None :
			n.cellspace[i] = T2.cellspace[i]
		elif T3.cellspace[i] is not None :
			n.cellspace[i] = T3.cellspace[i]
	n.cellspace[v] = myList()
	n.root = v
	
	# insertions
	INSERT(v, END(n.cellspace[v]), n.cellspace[v])
	INSERT(T3.root, END(n.cellspace[v]), n.cellspace[v])
	INSERT(T2.root, END(n.cellspace[v]), n.cellspace[v])
	INSERT(T1.root, END(n.cellspace[v]), n.cellspace[v])
	
	return n

# prints a tree.  Tadah!
# @param T	tree in question
def printTree(T) :
	for i in range(0, len(T.cellspace)) :
		if T.cellspace[i] is not None :
			print i,":",
			printList(T.cellspace[i])

# values are irrelephant, other than that they must be unique.
def buildTree(v, i) :
	if i == 0 :
		return CREATE0(v)
	else :
		return CREATE3(v, buildTree((3*i)-1, i-1), buildTree(3*i, i-1), buildTree((3*i)+1, i-1))

def herp() :
	gTree = buildTree(0, n)

def traverse(n, T) :
	if LEFTMOST_CHILD(n, T) is None :
		return
	else :
		traverse(LEFTMOST_CHILD(n, T), T)
		tmp = LEFTMOST_CHILD(n,T)
		tmp = RIGHT_SIBLING(tmp, T)
		while tmp is not None :
			traverse(tmp, T)
			tmp = RIGHT_SIBLING(tmp, T)

def derp() :
	gTree = buildTree(0, n)
	traverse(ROOT(gTree), gTree)

MAXNODES = 500
NUMREPS = 1000

gTree = tree()

for n in range(0, 5) :
	print "----- n = ", n, " -----"

	t = Timer("herp()", "from __main__ import herp")
	buildtime = t.timeit(NUMREPS)/(NUMREPS) # NUMREPS executions
	print "Time to build tree of size    ", n, ":\t", buildtime


	t = Timer("derp()", "from __main__ import derp")
	travtime = t.timeit(NUMREPS)/(NUMREPS) # NUMREPS executions
	print "Time to traverse tree of size ", n, ":\t", travtime-buildtime
