class myStack :
	def __init__(self) :
		data = None
		end = None # one past the last element
		return

def TOP(stk) :
	return stk.data[0]

def PUSH(val, stk) :
	# end is one past the last element
	stk.data[stk.end] = val
	stk.end += 1
	return

def POP(stk) :
	# no need to modify this data - simply sliding 'end' back will "remove" it
	stk.end -= 1
	return

def EMPTY(stk) :
	if stk.end == 0 :
		return True
	else :
		return False

def MAKENULL() :
	tmp = myStack()
	tmp.data = [0]*MAXLENGTH
	tmp.end = 0
	return tmp

def printStack(stk) :
	print stk.data[:stk.end]
	return


MAXLENGTH = 100


print "make new stack"
foo = MAKENULL()
printStack(foo)

print "pushing 1-5"
PUSH(1, foo)
PUSH(2, foo)
PUSH(3, foo)
PUSH(4, foo)
PUSH(5, foo)
printStack(foo)

print "pop twice"
POP(foo)
printStack(foo)
POP(foo)
printStack(foo)

print "is foo empty?"
print EMPTY(foo)

print "make foo empty"
foo = MAKENULL()

print "now is foo empty?"
print EMPTY(foo)