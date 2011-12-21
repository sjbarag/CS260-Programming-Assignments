import cmath 	# for complex version of exp()


i = cmath.sqrt(-1)


# @param x	Complex array
def FFT(x) :
	n = len(x)
	if n == 1 :
		return x[0]
	else :
		# initialize them so we can just append
		evenArray = []
		oddArray = []

		# split into even and odd arrays
		for r in range(n) :
			if r%2 == 0 :
				evenArray.append( x[r] )
			else :
				oddArray.append( x[r] )
		u = FFT(evenArray)
		v = FFT(oddArray)
		for s in range(n-1) :
			tau = cmath.exp(2 * cmath.pi * i * s / n)
			out[s] = u[ s % (n/2) ]  +  tau * v[ s % (n/2) ]
		return out


polynomial = [1, 2, 4]
print FFT(polynomial)
