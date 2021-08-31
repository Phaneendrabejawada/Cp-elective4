# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronic(s):
  if(s==0 or s==2 or s==6):
    return True
  k=int(s/2)
  for i in range(k):
    if(s==i*(i+1)):
      return True
  return False

def nthpronicnumber(n):
  found=0
  got=-1
  while(found<=n):
        got+=1
        if(pronic(got)):
            found+=1
  return got