class node :
	def __init__(self) :
		self.element = None
		self.lc  = None
		self.rc = None

	def __str__(self) :
		return str(self.element)

# tests for the presence of x in set A
# @param x	value to look for
# @param A	set that may or may not contain x
# @returns	true iff x in A; false otherwise
def MEMBER(x, A) :
	if A is None :
		return False
	elif x == A.element :
		return True
	elif x < A.element :
		return MEMBER(x, A.lc)
	elif x > A.element :
		return MEMBER(x, A.rc)

# inserts a new value x into the correct position in set A
# @param x	value to insert
# @param A	set that will contain x
def INSERT(x, A) :
	if A is None :
		A = node()
		A.element = x
		A.lc = None
		A.rc = None
	elif x < A.element :
		INSERT(x, A.lc)
	elif x > A.element :
		INSERT(x, A.rc)
	# if x == A.element, then x is already present.  We do nothing.

def INSERT(x, A) :
	tmp = A
	while tmp.lc is not None or tmp.rc is not None:
		if x < tmp.element :
			tmp = tmp.lc
		elif x > tmp.element :
			tmp = tmp.rc
		elif x == tmp.element :
			return
	A = node()
	A.element = x

# returns and removes the smallest element from set A
# @param A	set in question
def DELETEMIN(A) :
	if A.lc is None :
		# A points to smallest element
		A = A.rc	# replace A with its right child
		return A.element
	else :
		# A has a leftchild
		return DELETEMIN(A.lc)

# removes x from set A
# @param x	value to remove
# @param A	set containing x
def DELETE(x, A) :
	if A is not None :
		if x < A.element :
			DELETE(x, A.lc)
		elif x > A.element :
			DELETE(x, A.rc)
		# if we reach here, x == A.element
		elif A.lc is None and A.rc is None :
			A = None	# delete the leaf holding x
		elif A.lc is None :
			A = A.rc
		elif A.rc is None :
			A = A.lc
		else :
			# both children are present
			A.element = DELETEMIN(A.rc)

# counts the number of nodes on the path from the root of A to the node
# containing x
# @param x	value to search for
# @param A	set that may contain x
# @param i	current iteration of the recursive loop.  Probably an ugly way of
#			doing things.
# @retuns	the number of iterations of LOCATE required to arrive at x (and
# 			thus the number of nodes between the root of A and x), or None if x does not
# 			exist in A.
def LOCATE(x, A, i=0) :
	if A is None :
		return None
	elif x == A.element :
		return i
	elif x < A.element :
		return LOCATE(x, A.lc, i+1)
	elif x > A.element :
		return LOCATE(x, A.rc, i+1)


from random import shuffle

MAXVALUE = 10
values = range(0, MAXVALUE)
shuffle(values)
print values

BST = None

for e in values :
	INSERT(e, BST)
	print BST

for e in values :
	print LOCATE(e, BST)
