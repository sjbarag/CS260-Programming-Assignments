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
	
#	return temp

# return head of list
def FIRST(lst) :
	return lst.head

# return last node in list
def END(lst) :
	temp = lst.head
	while temp:	# may need change to while temp.nxt
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

# get node at specific position in list
def RETREIVE(pos, lst) :
	temp = FIRST(lst)
	for k in range(0, pos) :
		if temp.nxt != None :
			temp = temp.nxt
	return temp

# get next position in list
def NEXT(lst) :
	return (lst.cur).nxt


# convenience function to actually move to next position
def MOVENEXT(lst) :
	lst.cur = NEXT(lst)
	return

# get previous position in list
def PREVIOUS(lst) :
	temp = FIRST(lst)
	while temp :
		if temp.nxt == lst.cur :
			return temp
		else :
			temp = temp.nxt
	return None # no change if doesn't exist
	
# convenience function to actually move to next position
def MOVEPREVIOUS(lst) :
	lst.cur = PREVIOUS(lst)
	return

# tail insertion, returns nothing
def INSERT(val, lst) :
        # create new node with cargo 'val'
        tail = Node()
        # set it's 'cargo' field to the 'val' parameter
        tail.cargo = val
        # set it's 'nxt' field to None
        tail.nxt = None
        
        if lst.head is None :
                lst.head = tail
                lst.cur = tail
        else :
                # copy lst
                tmp = lst.head
                while tmp.nxt: # parse through tmp till end
                        tmp = tmp.nxt
                tmp.nxt = tail
                # copy tmp into lst
                lst = tmp # if this doesn't work, do everyting within lst
        
        return

def DELETE(pos, lst) :
	temp = FIRST(lst)
	# move to just before pos
	if pos == 0 :
		lst.head = temp.nxt
	else :
		while pos-1 > 0 :
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
			if FIRST(T.cellspace[i]) == n :
				return FIRST(T.cellspace[i]).nxt
	return None
			
#	if n in T.cellspace :
#		tmp = FIRST(T.cellspace[T.cellspace.index(n)])
#		print tmp
#		return NEXT(tmp)
#	else :
#		# n doesn't exist
#		return None

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
				return RETREIVE(p, T.cellspace[i]).nxt
	return None
					
# returns root node of a tree, or
# None if the tree is null.
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
	INSERT(v, n.cellspace[v])
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

	# insertions
	INSERT(v, n.cellspace[v])
	INSERT(T.root, n.cellspace[v])

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
	INSERT(v, n.cellspace[v])
	INSERT(T1.root, n.cellspace[v])
	INSERT(T2.root, n.cellspace[v])

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
	INSERT(v, n.cellspace[v])
	INSERT(T1.root, n.cellspace[v])
	INSERT(T2.root, n.cellspace[v])
	INSERT(T3.root, n.cellspace[v])
	
	return n

# prints a tree.  Tadah!
# @param T	tree in question
def printTree(T) :
	for i in range(0, len(T.cellspace)) :
		if T.cellspace[i] is not None :
			print i,":",
			printList(T.cellspace[i])
		
	

MAXNODES = 100
herp = CREATE0(1)
derp = CREATE0(2)
herpderp = CREATE2(5, herp, derp)
derpina = CREATE0(3)
foo = CREATE1(6, derpina)
bar = CREATE0(9)
final = CREATE3(10, foo, bar, herpderp)

print "tree 'final' as a list of of children."
print "[index : data]"
printTree(final)
print

n = ROOT(final)
print "root node: ", n

n = LEFTMOST_CHILD(n, final)
print "move to leftmost child: ", n

n = RIGHT_SIBLING(n, final)
print "move to right sibling: ", n

n = PARENT(n, final)
print "move to parent: ", n