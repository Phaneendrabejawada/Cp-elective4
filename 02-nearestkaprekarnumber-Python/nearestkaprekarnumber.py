# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def fun_nearestkaprekarnumber(n):
    nl=n
    nr=n
    cl=0
    cr=0
    fl=False
    fr=False
    while fl==False:
        if(isKaprekar(nl)):
            fl=True
        else:
            cl+=1
            nl-=1
    while fr==False:
        if(isKaprekar(nr)):
            fr=True
        else:
            cr+=1
            nr+=1
    if(cl<=cr):
        return nl
    if(cr<cl):
        return nr

def isKaprekar(n):
    if(n==1):
        return True
    dc=len(str(n*n))
    sq=n*n
    for i in range(dc-1):
        p=10**(i+1)
        if(p==n):
            continue
        s=(sq//p)+(sq%p)
        if(s==n):
            return True
    return False
