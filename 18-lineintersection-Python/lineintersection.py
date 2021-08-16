# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def ismultiple(m,n):
	if m == 0:
		return True
	if n == 0:
		return False
	if m % n == 0:
		return True
	else:
		return False

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	#checking for identical lines
	if(b1 == b2 or m1 == m2):
		return None
	if(ismultiple(m1,m2) or ismultiple(m2,m1)):
		return None
	else:
		return (abs(int(b2-b1)/(m1-m2)))
