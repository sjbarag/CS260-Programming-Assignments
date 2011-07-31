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

################################################################

MAXNODES = 100

foo = MAKENULL()
for i in range(6) :
	INSERT(i, 0, foo)
PRINTLIST(foo)

INSERT(7, END(foo), foo)
PRINTLIST(foo)

INSERT(12, 4, foo)
PRINTLIST(foo)

DELETE(3, foo)
PRINTLIST(foo)

print "first: ", RETRIEVE(FIRST(foo), foo)

print "location of 12: ", LOCATE(12, foo)

p = FIRST(foo)
p = NEXT(p, foo)
p = NEXT(p, foo)
p = NEXT(p, foo)
p = NEXT(p, foo)
print "data at position 4: ", RETRIEVE(p, foo)
p = PREVIOUS(p, foo)
print "data at position 3: ", RETRIEVE(p, foo)

print "data at end: ", RETRIEVE(END(foo), foo)
