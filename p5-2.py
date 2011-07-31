from timeit import Timer

class myList :
	def __init__(self) :
		self.data = [None]*MAXNODES
		self.end = 0 # one past last

# clear list
def MAKENULL() :
	return myList()

# return first position in list
# @param lst	list in question
def FIRST(lst) :
	if lst.end is 0 :
		return -1
	else :
		return 0

# return last position in list
# @param lst	list in question
def END(lst) :
	return lst.end

# find position of a specific value in the list
# @param val 	value to find
# @param lst	list in question
def LOCATE(val, lst) :
	for i in range(lst.end) :
		if lst.data[i] == val :
			return i

# get value at a specific position in the list
# @param pos	position to get data from
# @param lst	list in question
def RETRIEVE(pos, lst) :
	if pos > lst.end :
		return None
	else :
		return lst.data[pos]

# get next position in the list
# @param pos	position in question
# @param lst	list containing pos
def NEXT(pos, lst) :
	if pos > lst.end or pos + 1 > lst.end:
		return None
	else :
		return pos + 1

# get previous position in the list
# @param pos	position in question
# @param lst	list containing pos
def PREVIOUS(pos, lst) :
	if pos > lst.end or pos == 0 :
		return None
	else :
		return pos - 1

# inserts a value into a specific value in a list
# @param val	value to be inserted
# @param pos 	position to insert val
# @param lst	list to contain val
def INSERT(val, pos, lst) :	
	# out of bounds
	if pos > lst.end:
		return
	elif pos == lst.end :
		lst.data[pos] = val
	else :
		lst.data[pos+1:lst.end+1] = lst.data[pos:lst.end]
		lst.data[pos] = val
	# trim off any excess if theres a lot of data
	lst.data = lst.data[:MAXNODES]
	# shift end.
	lst.end += 1

# deletes the value at a spevific value in a list
# @param pos	position to delete
# @param lst	list in question
def DELETE(pos, lst) :
	if pos == lst.end :
		lst.end -= 1 # just chop off end - no need to change data
	else :
		lst.data[pos:lst.end-1] = lst.data[pos+1:lst.end]
		lst.end -= 1

# prints the list nicely
# @param lst	list in question
def PRINTLIST(lst) :
	print lst.data[0:lst.end]

######################################################################

# head insertion
def inshead() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(5, 0, lst)

def instail() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(5, END(lst), lst)

def trav() :
	# need something to traverse! using instail, as it should be faster	
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(5, END(lst), lst)

	p = FIRST(lst)
	while p :
		p = NEXT(p, lst)

def delhead() :
	# need something to traverse! using instail, as it should be faster	
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(5, END(lst), lst)

	for i in range(0, n) :
		DELETE(0, lst)

def deltail() :
	# need something to traverse! using instail, as it should be faster	
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(5, END(lst), lst)

	for i in range(0, n) :
		DELETE(END(lst), lst)

# control for assignment
def assignment() :
	lst = MAKENULL()

NUMREPS = 100
for i in range(1, 4) :
	n = 10**i
	MAXNODES = n

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
	print "Time per traversal:      \t", travtime-asgntime
	
	t = Timer("delhead()", "from __main__ import delhead")
	delheadtime = t.timeit(NUMREPS)/(NUMREPS*n) # NUMREPS executions * n ops
	print "Time per head deletion: \t", delheadtime-asgntime
	
	t = Timer("deltail()", "from __main__ import deltail")
	deltailtime = t.timeit(NUMREPS)/(NUMREPS*n) # NUMREPS executions * n ops
	print "Time per tail deletion: \t", deltailtime-asgntime
	print
