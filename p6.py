def DIJKSTRA(C):
	"""
	computes the cost of the shortest paths from vertex 0 to every vertex of a
	directed graph

	param C		n x n array of costs
	"""
	global n
	global p
	V = range(0, n)
	S = [0]
	D = []
	for i in range(n) :
		D.append(None)
	#D = []*n
	for i in range(1, n) :
		D[i] = C[0][i]
		p[i] = 0
	for i in range(n-1) :
		Ds = []
		vMinusS = [j for j in V if j not in S]
		for k in vMinusS:		# thanks, StackOverflow!
			Ds.append(D[k])							# as with DFS, there was no
													#   requirement to not use
													#   the built-in list types.
													#   I am using them merely
													#   for convenience.
		w = min(Ds)
		S.append(w)
		for v in vMinusS :
			if D[v] > D[w] + C[w][v] :
				D[v] = D[w] + C[w][v]
				p[v] = w


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
	  [0, 0, 0, 0, 0,  0] ]

p = [0, 0, 0, 0, 0, 0]

print p
DIJKSTRA(c)
print p
