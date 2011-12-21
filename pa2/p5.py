class Node:
	def __init__(self):
		self.cargo = None
		self.nxt = None
		self.child = None

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

def GETNODE(pos, lst) :
	temp = FIRST(lst)
	for k in range(0, pos) :
		if temp.nxt != None :
			temp = temp.nxt
	return temp

# get next position in list
def NEXT(n) :
	return n.nxt



# get previous position from node
def PREVIOUS(n, lst) :
	temp = FIRST(lst)
	while temp :
		if temp.nxt == n :
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

# @param letter		letter to be added to the trie
# @param lst		list to be parent of letter
# @return 		the new node
def ADD_CHILD(letter, lst) :
	l = myList()
	n = Node()
	n.cargo = letter
	lst.child = l
	l.head = n
	l.cur = l.head
	return l



def ADD_WORD(word, lst) :
	global wc
	L = lst
	for letter in word :
		if L is not None :
			if LOCATE(letter, L) == -1 :
				# add node to end of current list
				INSERT(letter, END(L), L)
				# move to current list
				#L = END(L)
				# letter doesn't exist, so add the rest of them
				for ltr in word[word.index(letter)+1:] :
					t = ADD_CHILD(ltr, L)
					L = t
				ADD_CHILD('$', L)
				wc += 1
				return lst
			else :
				# move to appropriate child
				L = GETNODE(LOCATE(letter, L), L).child
		else :
			# create a first node
			L = MAKENULL()
			INSERT(letter, END(L), L)
			# move to current list
			L = END(L)
			# letter doesn't exist, so add the rest of them
			for ltr in word[word.index(letter)+1:] :
				t = ADD_CHILD(ltr, L)
				L = t
			ADD_CHILD('$', L)
			wc += 1
			return lst
	return lst

Trie = MAKENULL()

global wc
wc = 0
import sys
for rawline in sys.stdin.readlines() :
	cleanline = rawline.strip().split(' ')
	for word in cleanline :
		Trie = ADD_WORD(word.lower(), Trie)

print "Size of the trie = number of leaf nodes in trie ="
print "    number of '$'s inserted into trie."
print "Trie size: ", wc
