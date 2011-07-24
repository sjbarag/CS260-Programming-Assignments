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

# get data at specific position in list
def RETREIVE(pos, lst) :
	temp = FIRST(lst)
	for k in range(0, pos) :
		if temp.nxt != None :
			temp = temp.nxt
	return temp.cargo

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

# head insertion, returns new head
def INSERT(val, lst) :
	# create new node with cargo 'val'
	head = Node()
	# set it's 'cargo' field to the 'val' parameter
	head.cargo = val
	# set it's 'nxt' field to the current list header
	head.nxt = lst.head
	# change the current header to the newly created node
	lst.head = head
	# change the current position to the new list head
	lst.cur = lst.head
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


foo = MAKENULL()
INSERT(1, foo)
INSERT(2, foo)
INSERT(3, foo)
INSERT(4, foo)
print "foo: "
# should be 4 3 2 1
printList(foo)

DELETE(1, foo)
print "deleted position 1"
#should be 4 2 1
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
INSERT(5, foo)
printList(foo)
