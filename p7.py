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
	elif pos == FIRST(lst) and FIRST(lst) != END(lst):
		print val,"position is FIRST"
		# set n's 'nxt' field to the current list header
		n.nxt = lst.head
		# change the current header to the newly created node
		lst.head = n
		# change the current position to the new list head
		lst.cur = lst.head
		return
	else :
	        n.nxt = None
        
	        if lst.head is None :
	                lst.head = n
	                lst.cur = n
	        else :
	                # copy lst
	                tmp = lst.head
	                while tmp.nxt: # parse through tmp till end
	                        tmp = tmp.nxt
	                tmp.nxt = n
	                # copy tmp into lst
	                lst = tmp 	        
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

def merge(lst1, lst2) :
	out = MAKENULL()
	A = FIRST(lst1)
	B = FIRST(lst2)
	while A and B :
		if A.cargo <= B.cargo :
			INSERT(A.cargo, END(out), out)
			A = A.nxt
		else :
			INSERT(B.cargo, END(out), out)
			B = B.nxt
	
	# a is longer
	if A is not None and B is None :
		while A :
			INSERT(A.cargo, END(out), out)
			A = A.nxt
	elif B is not None and A is None :
		while B :
			INSERT(B.cargo, END(out), out)
			B = B.nxt
	return out
	


foo = MAKENULL()
bar = MAKENULL()
for i in range(0, 10, 2) :
	INSERT(i, END(foo), foo)
	INSERT(i+5, END(bar), bar)
printList(foo)
printList(bar)
foobar = merge(foo, bar)
printList(foobar)
