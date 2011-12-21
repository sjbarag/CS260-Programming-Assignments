def DFS(v) :
	"""
	performs depth-first search, and prints the current node
	@param v		the current node in the search
	""" # I finally switched to Pythonic documentation syntax.  Not too sure if I like it...
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
# NOTE: A..F has be remapped to 0..5 to make things simpler for the creation of the adjacency list.  These numbers are translated back into letters before printing.
# adjacency list, taken from figure 6.38 (page 226).  I am using Python's
#   built-in list type here for simplicity, as there does not appear to be a
#   requirement to use my own implementation.
L = [ [1, 3, 5], \
	  [2, 5], \
	  [3], \
	  [1], \
	  [3, 5], \
	  [3] ]

print "Results of Depth-first Search, starting at 'A,' for the directed graph in Figure 6.38:"
for v in range(NUMNODES) :
	if not mark[v] :
		DFS(v)
