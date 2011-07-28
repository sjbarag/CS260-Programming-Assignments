class Node:
        def __init__(self):
                self.cargo = None
                self.nxt = None
        
        def __str__(self):
                return str(self.cargo)  
 
class myQueue:
        def __init__(self):
                self.front = None
                self.cur = None
                
  
# clear list
def MAKENULL() :
        temp = myQueue()
        front = Node()
        cur = front
        
        return temp

# return head of list
def FRONT(q) :
        return q.front
 
# tail insertion
def ENQUEUE(val, q) :
        # create new node with cargo 'val'
        tail = Node()
        # set it's 'cargo' field to the 'val' parameter
        tail.cargo = val
        # set it's 'nxt' field to None
        tail.nxt = None
        
        if EMPTY(q) :
        	q.front = tail
        	q.cur = tail
        else :
	        # copy q
	        tmp = q.front
	        while tmp.nxt: # parse through tmp till end
	        	tmp = tmp.nxt
	        tmp.nxt = tail
		# copy tmp into q
		q = tmp	# if this doesn't work, do everyting within q
	
        return

# delete from front
def DEQUEUE(q) :
        q.front = q.front.nxt
        q.cur = q.front

	return
	
def EMPTY(q) :
	if q.front is None :
		return True
	else :
		return False

def printQueue(q) :
        temp = FRONT(q)
        if temp is None :
                print "(empty)",
        else :
                while temp :
                        print temp,
                        temp = temp.nxt
        print
 
foo = MAKENULL()
print "enqeue four times"
for i in range(1,5) :
	ENQUEUE(i, foo)
	if i != 4 :
		printQueue(foo)
print "foo: "
# should be 1 2 3 4
printQueue(foo)
 
DEQUEUE(foo)
print "dequeue one"
#should be 2 3 4
printQueue(foo)

print "is foo empty?"
print EMPTY(foo)

print
print
 
print "making foo null"
foo = MAKENULL()
printQueue(foo)
print "is foo empty?"
print EMPTY(foo)
 
print "adding 5 to foo"
ENQUEUE(5, foo)
printQueue(foo)