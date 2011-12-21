probeCount = 0
# hashes a word using Python's builtin __hash__ function
# @param word	word to hash
# @return	bucket (out of B possibilities) for word
def h(word) :
	return hash(word) % B

# creates null dictionary
def MAKENULL() :
	tmp = []
	for i in range(B) :
		tmp.append(None)	# I probably could use `tmp = [None]*B` but I had
							# issues where all the elements maintained the same data before, hence the for
							# loop.
	return tmp

def LOCATE(word, D) :
	global g_probeCount
	initial = h(word)
	i = 0
	while ( i < B ) and ( D[ (initial + i) % B ] != word ) and ( D[ (initial + i) % B ] is not None ) :
		i += 1
	g_probeCount += i
	return  (initial + i) % B

# checks to see if word is in D
# @param word 	word to test
# @param D	dictionary that may or may not contain D
# @returns	True if word exists in D; False otherwise
def MEMBER(word, D) :
	return D[ LOCATE(word, D) ] == word

# inserts a word into the appropriate bucket in D, provided the word is not already there
# @param word	word to insert
# @param D	dictionary to contain word
def INSERT(word, D) :
	bucket = LOCATE(word, D)
	if D[ bucket ] == word :		# word is already present
		return
	elif D[ bucket ] is None :		# locate found an empty spot
		D[ bucket ] = word
	return

# deletes a word from its bucket in D.  Does not test if it exists first, as that is lossy
# @param word	word to delete
# @param D	dictionary from which word will be deleted
def DELETE(word, D) :
	bucket = LOCATE(word, D)
	if bucket != -1 :
		D[bucket] = None
	return


probeListI = []
avgListI = []
probeListD = []
avgListD = []
bList = []
oList = []
global g_probeCount
g_probeCount = 0


# save from stdin and count words
import sys
inputLines = []
wc = 0
for raw in sys.stdin.readlines() :
	inputLines.append(raw)
	wc += len(raw.split(' '))

B = 1
for B in range(1, wc+100, 1000) :
	# I like even numbers :)
	if B != 1 :
		B = B -1

	DICTIONARY = MAKENULL()
	g_probeCount = 0

	for raw in inputLines :
		line = raw.strip().split(' ')
		for w in line :
			INSERT(w, DICTIONARY)
	#val = float(wc)/float(B)
	#val = float(1) - val
	#val = float(1)/float(val)
	#val = float(1) + val
	#val = val/float(2)
	#val = 1 + (float(1)/float(1 - (float(wc)/float(B))) )
	bList.append(B)
	#oList.append(val)
	probeListI.append(g_probeCount)
	avgListI.append( float(g_probeCount/float(wc)) )

	g_probeCount = 0
	for raw in inputLines :
		line = raw.strip().split(' ')
		for w in line :
			DELETE(w, DICTIONARY)

	probeListD.append(g_probeCount)
	avgListD. append( float(g_probeCount/float(wc)) )

print "Number of words: " +str(wc)
print "  \tInsert \t\tDelete \t\tInsert \tDelete"
print "  \tTotal  \t\tTotal  \t\tAverage \t\tAverage"
print "B \tProbes \t\tProbes \t\tProbes  \t\tProbes"
print "-" *88
for i in range(len(probeListI)) :
	print str(bList[i]) +"\t" +str(probeListI[i]) +"\t\t" +str(probeListD[i]) +"\t\t", avgListI[i], "\t\t", avgListD[i]
	#print str(bList[i]) +"\t" +str(probeListI[i]) +"\t\t", avgListI[i]
	#print str(bList[i]) +"\t" + str(oList[i]) +"\t" +str(probeListI[i]) +"\t\t", avgListI[i]
