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

MAXNODES = 100

# ordering taken from the following binary tree:
#          A
#       /     \
#     B         C
#   /   \     /   \
#  D     E   F     G
# / \   / \ / \   / \
# H I  J  K L M   N O

pre = ['A', 'B', 'D', 'H', 'I', 'E', 'J',  'K', 'C', 'F', 'L', 'M', 'G', 'N', 'O']
post = pretopost(pre)
print post

pre2 = posttopre(post)
print pre2

inorder = pretoin(pre)
print inorder
