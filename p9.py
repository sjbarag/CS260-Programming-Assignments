def DFS(v) :
	"""performs depth-first search"""
	global mark
	global L
	print LETTERS[v],
	mark[v] = True
	for w in L[v] :
		if not mark[w] :
			DFS(w)

NUMNODES = 6
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f']
mark = [False]*NUMNODES
# NOTE: A..F has be remapped to 0..5 to make things simpler.  This could be
#   done with letters, but everything would need to be hashed first
# adjacency list, taken from figure 6.38 (page 226).  I am using Python's
#   built-in list type here for simplicity, as there does not appear to be a
#   requirement to use my own implementation.
L = [ [1, 3, 5], \
	  [2, 5], \
	  [3], \
	  [1], \
	  [3, 5], \
	  [3] ]

for v in range(NUMNODES) :
	if not mark[v] :
		DFS(v)
