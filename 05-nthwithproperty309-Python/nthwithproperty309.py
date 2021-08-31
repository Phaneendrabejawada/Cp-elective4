# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def withproperty309(n):
	x = n ** 5
	y = str(x)
	z = '0123456789'
	for i in z:
		if(i in y):
			continue
		else:
			return False
	return True

def nthwithproperty309(n):
	# Your code goes here
	a = -1
	b = 0
	while(a < n):
		b = b + 1
		if(withproperty309(b)):
			a = a + 1
	return b