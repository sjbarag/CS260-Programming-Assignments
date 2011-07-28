class Node:
        def __init__(self):
                self.cargo = None
                self.nxt = None
        
        def __str__(self):
                return str(self.cargo)  
 
class myStack:
        def __init__(self):
                self.top = None
  
# clear list
def MAKENULL() :
        temp = myStack()
        
        return temp

# return head of list
def TOP(lst) :
        return lst.top
 
# head insertion, returns new head
def PUSH(val, lst) :
        # create new node with cargo 'val'
        top = Node()
        # set it's 'cargo' field to the 'val' parameter
        top.cargo = val
        # set it's 'nxt' field to the current list header
        top.nxt = lst.top
        # change the current header to the newly created node
        lst.top = top

        return
 
def POP(lst) :
        lst.top = lst.top.nxt

	return
	
def EMPTY(lst) :
	if lst.top is None :
		return True
	else :
		return False

def printStack(lst) :
        temp = TOP(lst)
        if temp is None :
                print "(empty)",
        else :
                while temp :
                        print temp,
                        temp = temp.nxt
        print
 
 
foo = MAKENULL()
print "push four times"
for i in range(1,5) :
	PUSH(i, foo)
	if i != 4 :
		printStack(foo)
print "foo: "
# should be 4 3 2 1
printStack(foo)
 
POP(foo)
print "pop one"
#should be 3 2 1
printStack(foo)

print "is foo empty?"
print EMPTY(foo)

print
print
 
print "making foo null"
foo = MAKENULL()
printStack(foo)
print "is foo empty?"
print EMPTY(foo)
 
print "adding 5 to foo"
PUSH(5, foo)
printStack(foo)