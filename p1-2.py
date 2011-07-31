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


foo = MAKENULL()
INSERT(1, 0, foo)
INSERT(2, 0, foo)
INSERT(3, 0, foo)
INSERT(4, 0, foo)
print "foo: "
# should be 4 3 2 1
printList(foo)


INSERT(7, 3, foo)
INSERT(8, 5, foo)
print "foo: "
# should be 4 3 2 7 1 8
printList(foo)

DELETE(1, foo)
print "deleted position 1"
#should be 4 2 1
printList(foo)

DELETE(END(foo), foo)
printList(foo)

print "moving to next position"
# should be 2
print NEXT(foo)
MOVENEXT(foo)
printList(foo)

print "moving back to previous position"
# should be 4
print PREVIOUS(foo)
MOVEPREVIOUS(foo)
printList(foo)

print "locating position of '1'"
# should be 2
print LOCATE(1, foo)

print "retreiving value at position '2'"
# should be 1
print RETREIVE(2, foo)

print
print

print "making foo null"
foo = MAKENULL()
printList(foo)

print "adding 5 to foo"
INSERT(5, 0, foo)
printList(foo)
