# hashes a word using Python's builtin __hash__ function
# @param word	word to hash
# @return	bucket (out of B possibilities) for word
def h(word) :
	return hash(word) % B

# creates null dictionary
def MAKENULL() :
	tmp = []
	for i in range(B) :
		tmp.append(None)	# I probably could use `tmp = [None]*B` but I had issues where all the elements maintained the same data before, hence the for loop.
	return tmp

# finds the location of word in D
# @param word	word to find
# @param D	dictionary to contain word
# @returns 	index in D of word, or -1 if not found
def LOCATE(word, D) :
	i = h(word)
	if D[i] == word :
		return i
	else :
		j = (i+1)%B
		while j != i :
			if D[j] == word :
				return j
			else :
				j = (j+1)%B
		return -1
		
# checks to see if word is in D
# @param word 	word to test
# @param D	dictionary that may or may not contain D
# @returns	True if word exists in D; False otherwise
def MEMBER(word, D) :
	if LOCATE(word, D) != -1 :
		return True
	else :
		return False
		
# inserts a word into the appropriate bucket in D, provided the word is not already there
# @param word	word to insert
# @param D	dictionary to contain word
def INSERT(word, D) :
	if not MEMBER(word, D) :
		bucket = h(word)
		if D[bucket] is None :
			D[bucket] = word
		else :
			i = (bucket+1)%B
			while i != bucket :
				if D[i] is None :
					D[i] = word
					return
				else :
					i = (i+1)%B
	return

# deletes a word from its bucket in D.  Does not test if it exists first, as that is lossy
# @param word	word to delete
# @param D	dictionary from which word will be deleted
def DELETE(word, D) :
	bucket = LOCATE(word, D)
	if bucket != -1 :
		D[bucket] = None
	return


B = 10
#DICTIONARY = MAKENULL()
DICTIONARY = ['ligula', 'ipsum', 'adipiscing', 'sit', 'Lorem', 'dolor', 'consectetur', 'amet', 'elit', 'Phasellus']


countList = []

import sys
for raw in sys.stdin.readlines() :
	line = raw.strip().split(' ')
	for w in line :
		DELETE(w, DICTIONARY)
print DICTIONARY
#total = 0
#for e in countList :
#	total += float(e)
#print float(total/float(len(countList)))