def pretopost(lst) :
	if len(lst) == 3 :
		tmp = lst[:]
		tmp[0:2] = lst[1:3]
		tmp[2] = lst[0]
		return tmp
	else :
		tmp = lst
		tmp = pretopost(lst[1:((len(lst)+1)/2)]) + pretopost(lst[((len(lst)+1)/2):]) + [lst[0]]
		return tmp
		
def posttopre(lst) :
	if len(lst) == 3 :
		tmp = lst[:]
		tmp[1:3] = lst[0:2]
		tmp[0] = lst[2]
		return tmp
	else :
		tmp = [lst[-1]] + posttopre( lst[ 0 : ( (len(lst)-1) /2) ] ) + posttopre( lst[ ( (len(lst)-1) /2) : -1 ] )
		return tmp

def pretoin(lst) :
	if len(lst) == 3 :
		tmp = lst[:]
		t = tmp[0]
		tmp[0] = lst[1]
		tmp[1] = t
		return tmp
	else :
		tmp = lst
		tmp = pretoin( lst[ 1 : ( (len(lst)+1) /2) ] ) + [lst[0]] + pretoin( lst[ ((len(lst)+1) /2) : ] )
		#tmp = pretoin( lst[ 0 : ( (len(lst)-1) /2) ] ) + [lst[ (len(lst)-1)/2 ]] + pretoin( lst[ ( (len(lst)+1) /2): ] )
		return tmp

def calcpost(lst) :
	if len(lst) == 3 :
		# ew, python doesn't have a switch/case statement.  There's ways to
		# hack it, but it doesn't seem worth it for four cases.
		if lst[-1] == '+' :
			return lst[0] + lst[1]
		elif lst[-1] == '-' :
			return lst[0] - lst[1]
		elif lst[-1] == '*' :
			return lst[0] * lst[1]
		elif lst[-1] == '/' :
			return lst[0] / lst[1]
		elif lst[-1] == '%' :
			return lst[0] % lst[1]
	else :
		if lst[-1] == '+' :
			return calcpost( lst [ : ( (len(lst)-1)/2) ] )  +   calcpost( lst [ ((len(lst) - 1)/2) : -1] )
		elif lst[-1] == '-' :
			return calcpost( lst [ : ( (len(lst)-1)/2) ] )  -   calcpost( lst [ ((len(lst) - 1)/2) : -1] )
		elif lst[-1] == '*' :
			return calcpost( lst [ : ( (len(lst)-1)/2) ] )  *   calcpost( lst [ ((len(lst) - 1)/2) : -1] )
		elif lst[-1] == '/' :
			return calcpost( lst [ : ( (len(lst)-1)/2) ] )  /   calcpost( lst [ ((len(lst) - 1)/2) : -1] )
		elif lst[-1] == '%' :
			return calcpost( lst [ : ( (len(lst)-1)/2) ] )  %   calcpost( lst [ ((len(lst) - 1)/2) : -1] )
			
def calcpre(lst) :
	if len(lst) == 3 :
		# ew, python doesn't have a switch/case statement.  There's ways to
		# hack it, but it doesn't seem worth it for four cases.
		if lst[0] == '+' :
			return lst[1] + lst[2]
		elif lst[0] == '-' :
			return lst[1] - lst[2]
		elif lst[0] == '*' :
			return lst[1] * lst[2]
		elif lst[0] == '/' :
			return lst[1] / lst[2]
		elif lst[0] == '%' :
			return lst[1] % lst[2]
	else :
		if lst[0] == '+' :
			return calcpre( lst [ 1 : ( (len(lst)+1)/2) ] )  +   calcpre( lst [ (len(lst) + 1)/2 : ] )
		elif lst[0] == '-' :
			return calcpre( lst [ 1 : ( (len(lst)+1)/2) ] )  -   calcpre( lst [ (len(lst) + 1)/2 : ] )
		elif lst[0] == '*' :
			return calcpre( lst [ 1 : ( (len(lst)+1)/2) ] )  *   calcpre( lst [ (len(lst) + 1)/2 : ] )
		elif lst[0] == '/' :
			return calcpre( lst [ 1 : ( (len(lst)+1)/2) ] )  /   calcpre( lst [ (len(lst) + 1)/2 : ] )
		elif lst[0] == '%' :
			return calcpre( lst [ 1 : ( (len(lst)+1)/2) ] )  %   calcpre( lst [ (len(lst) + 1)/2 : ] )

MAXNODES = 100

# ordering taken from the following binary tree:
#        *
#      /   \
#    +       +
#   / \     / \
#  5   3   5   2

pre = ['*', '+', 5, 3, '+', 5, 2]
print pre
print calcpre(pre)

post = [2, 7, '+', 3, 4, '+', '*']
print post
print calcpost(post)

#post = pretopost(pre)
#print post
#
#pre2 = posttopre(post)
#print pre2
#
#inorder = pretoin(pre)
#print inorder
