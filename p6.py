def DIJKSTRA2() :
	"""
	computes the cost of the shortest paths from vertex 0 to every vertex of a
	directed graph

	param C		n x n array of costs
	"""
	global n
	S = [0]
	V = range(n)
	D = [0, 0, 0, 0, 0, 0]
	C = [ [ 0,  4,  1,  5,  8, 10], \
		  [50,  0, 50, 50, 50, 50], \
	  	  [50,  2,  0, 50, 50, 50], \
	  	  [50, 50, 50,  0,  2, 50], \
		  [50, 50, 50, 50,  0,  1], \
		  [50, 50, 50, 50, 50,  0] ]
	P = [None, None, None, None, None, None]
	for i in range(1,n) :
		D[i] = C[0][i]
	for i in range(n-1) :
		vMinusS = [e for e in V if e not in S]
		w = min([ D[f] for f in vMinusS ])
		w = D.index(w)
		if w not in S :
			S.append(w)

		vMinusS = [e for e in V if e not in S]
		for v in vMinusS :
			if D[w] + C[w][v] < D[v] :
				P[v] = w
			D[v] = min( D[v], D[w] + C[w][v] )
	print "Intermediaries:", P
	return D




global n
n = 6

# initialize!
c = [ [ 0,  4,  1,  5,  8, 10], \
	  [50,  0, 50, 50, 50, 50], \
	  [50,  2,  0, 50, 50, 50], \
	  [50, 50, 50,  0,  2, 50], \
	  [50, 50, 50, 50,  0,  1], \
	  [50, 50, 50, 50, 50,  0] ]

# these aren't very Pythonic, but [[0]*n]*n resulted in each row being a copy
#   of the first one, including later assignments.
a = [ [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0], \
	  [0, 0, 0, 0, 0,  0] ]


#print DIJKSTRA2(c)
dist = DIJKSTRA2()
print "Final distances: "
for i in range(n) :
	print "0 ->", i, ":", dist[i]
