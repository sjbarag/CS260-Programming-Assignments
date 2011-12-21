def SHORTEST(A, C, P) :
	"""
	Produces a matrix of lengths of shortest paths and a matrix giving a point in the 'middle' of each shortest path

	param A		n x n matrix of shotest paths
	param C		n x n matrix of arc costs
	param P		n x n matrix giving a point in the 'middle' of each shortest path
	"""
	global n
	for i in range(n) :
		for j in range(n) :
			A[i][j] = C[i][j]
			P[i][j] = 0
			#P[i,j] = None	# using None in place of 0, as arrays are 0-indexed in Python.
	for i in range(n) :
		A[i][i] = 0
	for k in range(n) :
		for i in range(n) :
			for j in range(n) :
				if A[i][k] + A[k][j] < A[i][j] :
					A[i][j] = A[i][k] + A[k][j]
					P[i][j] = k

def PATH(i, j) :
	global p
	P = p
	"""
	Prints the shortest path between two nodes

	param i		starting node
	param j		destination node
	"""
	k = P[i][j]
	if k == 0 :
		return
	PATH(i, k)
	print k
	PATH(k, j)

global n
n = 6

# initialize!
c = [ [0, 4, 1, 5, 8, 10], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 2, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 2,  0], \
	  [0, 0, 0, 0, 0,  1], \
	  [0, 0, 0, 0, 0,  0] ]

# these aren't very Pythonic, but [[0]*n]*n resulted in each row being a copy
#   of the first one, including later assignments.
a = [ [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0]]

p = [ [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0]]

print "Initial Cost Matrix (C):"
for e in c :
	print e


SHORTEST(a, c, p)
print
print "Final Path Matrix (P):"
for e in p :
	print e

print
print "Path Intermediates:"
print "0->1"
PATH(0,1)
print
print "0->2"
PATH(0,2)
print
print "0->3"
PATH(0,3)
print
print "0->4"
PATH(0,4)
print
print "0->5"
PATH(0,5)
