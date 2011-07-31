from timeit import Timer

# head insertion
def inshead() :
	lst = [0]*n
	for i in range(0, n) :
		lst.insert(0, 5)

# tail insertion
def instail() :
	lst = [0]*n
	for i in range(0, n) :
		lst.append(5)
	
# list traversal
def trav() :
	lst = [0]*n
	for i in range(len(lst)) :
		x = lst[i]

# head deletion
def delhead() :
	lst = [0]*n
	for i in range(0, n) :
		del lst[0]

# tail deletion
def deltail() :
	lst = [0]*n
	for i in range(0, n) :
		del lst[-1]

# control timer for assignment.  used to normalize timings that contain an assignment
def assignment() :
	lst = [0]*n

NUMREPS = 10000
for i in range(1, 4) :
	n = 10**i

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
