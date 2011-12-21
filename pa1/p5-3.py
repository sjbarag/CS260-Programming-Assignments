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
def MAKENULL() :
	temp = myList()
	
	return temp

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
	return temp.cargo

# get next position from node
def NEXT(n) :
	return n.nxt
	

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

######################################################################

# head insertion
def inshead() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(i, 0, lst)

def instail() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(i, END(lst), lst)

def trav() :
	# need something to traverse! (using inshead because it's O(1))
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(i, 0, lst)

	tmp = FIRST(lst)
	while tmp :
		tmp = NEXT(tmp)

def delhead() :
	# need something to traverse! (using inshead because it's O(1))
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(i, 0, lst)

	for i in range(0, n) :
		DELETE(0, lst)

def deltail() :
	# need something to traverse! (using inshead because it's O(1))
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(i, 0, lst)

	for i in range(0, n) :
		DELETE(END(lst), lst)

# control timer for assignment.  used to normalize timings that contain an assignment
def assignment() :
	lst = MAKENULL()

NUMREPS = 100
# It's reeaaaaallly slow if I do range(1, 5) - I left it running for several
# minutes on a reasonably modern machine and it still hadn't finished.
for i in range(1, 4) :
	n = 10**i

	print "----- n = ", n, " -----"

	t = Timer("assignment()", "from __main__ import assignment")
	asgntime = t.timeit(NUMREPS)/(NUMREPS*n) # NUMREPS executions * n ops
	
	t = Timer("inshead()", "from __main__ import inshead")
	insheadtime = t.timeit(NUMREPS)/(NUMREPS*n) # NUMREPS executions * n ops
	print "Time per head insertion: \t", insheadtime-asgntime
	
	t = Timer("instail()", "from __main__ import instail")
	instailtime = t.timeit(NUMREPS)/(NUMREPS*n) # NUMREPS executions * n ops
	print "Time per tail insertion: \t", instailtime-asgntime

	t = Timer("trav()", "from __main__ import trav")
	travtime = t.timeit(NUMREPS)/(NUMREPS*n) # NUMREPS executions * n ops
	print "Time per traversal:      \t", travtime-insheadtime

	t = Timer("delhead()", "from __main__ import delhead")
	delheadtime = t.timeit(NUMREPS)/(NUMREPS*n) # NUMREPS executions * n ops
	print "Time per head deletion: \t", delheadtime-insheadtime
	
	t = Timer("deltail()", "from __main__ import deltail")
	deltailtime = t.timeit(NUMREPS)/(NUMREPS*n) # NUMREPS executions * n ops
	print "Time per tail deletion: \t", deltailtime-insheadtime
	print
	
