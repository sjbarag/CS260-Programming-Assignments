# hashes a word using Python's builtin __hash__ function
# @param word	word to hash
# @return	bucket (out of B possibilities) for word
def h(word) :
	return hash(word) % B

class Node :
	def __init__(self) :
		self.val = None
		self.nxt = None

	def __str__(self) :
		return str(self.val)

# creates null dictionary
def MAKENULL() :
	tmp = []
	for i in range(B) :
		tmp.append(None)
	return tmp

# checks to see if word is in D
# @param word 	word to test
# @param D	dictionary that may or may not contain D
# @return	True if word exists in D; False otherwise
def MEMBER(word, D) :
	cProbe = 1
	c = D[h(word)]
	while c is not None :
		if c.val == word :
			#print cProbe
			#print countList
			countList.append(cProbe)
			return True
		else :
			c = c.nxt
			cProbe += 1
	countList.append(cProbe)
	return False

# inserts a word into the appropriate bucket in D, provided the word is not already there
# @param word	word to insert
# @param D	dictionary to contain word
def INSERT(word, D) :
	if not MEMBER(word, D) :
		# get correct bucket by hashing
		bucket = h(word)
		# save old head
		oldhead = D[bucket]
		# create new node and fill its fields appropriately (head insertion)
		n = Node()
		n.val = word
		n.nxt = oldhead
		# set the new node as the first in the bucket
		D[bucket] = n
	return

# deletes a word from its bucket in D.  Does not test if it exists first, as that is lossy
# @param word	word to delete
# @param D	dictionary from which word will be deleted
def DELETE(word, D) :
	bucket = h(word)
	if D[bucket] is not None :
		if D[bucket].val == word :	# word is the first node
			D[bucket] = D[bucket].nxt
		else :	# c isn't in the first node.  This doesn't mean it exists at all, just that it wasn't first.
			c = D[bucket]
			# search
			while c.nxt is not None :
				if c.nxt.val == word :
					c.nxt = c.nxt.nxt	# remove word form list
				else :
					c = c.nxt		# move to next node
			return

# prints a dictionary nicely
# @param D	dictionary to print
def printDict(D) :
	for i in range(len(D)) :
		if D[i] is not None :
			c = D[i]
			print "[",
			while c is not None :
				print c,
				c = c.nxt
			print "]"
	return


# used for each loop
countList = []
inputlines = []

bList = []
probeList = []
avgList = []

# save from stdin
import sys
for raw in sys.stdin.readlines():
	inputlines.append(raw)

for B in range(1, 15002, 250) :
	# I like even numbers :)
	if B != 1 :
		B = B - 1
	DICTIONARY = MAKENULL()
	
	countList = []
	for raw in inputlines :
		line = raw.strip().split(' ')
		for w in line :
			INSERT(w, DICTIONARY)
	
	# number of probes is O(1 + (n/B) )
	# worst case of this is B = 1 (all elements in same bucket)
	# this would require one probe for each element and one more for ... something.
	
	total = 0
	for e in countList :
		total += float(e)
	#print "Number words:\t", len(countList)
	#print "-"*30
	#print "B:\t\t", B
	#print "Total probes:\t", total
	#print "Average probes:\t", float(total/float(len(countList)))
	bList.append(B)
	probeList.append(total)
	avgList.append(float(total/float(len(countList))))

print "Number of words: " +str(len(countList))
print "  \tTotal  \t\tAverage"
print "B \tProbes \t\tProbes"
print "-"*37
for i in range(len(bList)) :
	print str(bList[i]) +"\t" + str(probeList[i]) + "  \t", avgList[i]
