class myStack :
	def __init__(self) :
		data = None
		return


def TOP(stk) :
	return stk.data[0]

def PUSH(val, stk) :
	stk.data.append(val)
	return

def POP(stk) :
	stk.data.pop()
	return

def EMPTY(stk) :
	if len(stk.data) == 0 :
		return True
	else :
		return False

def MAKENULL() :
	tmp = myStack()
	tmp.data = []
	return tmp

def printStack(stk) :
	print stk.data
	return

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