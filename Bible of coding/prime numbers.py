# to find prime number , this approach's time complexity is O(n)
import math
def primeNormal(item):
    result=True
    for i in range(2,item ):
        if item % i == 0:
            result = False
            break
    return result
def primeBest(item):
    result=True
    # this works on the principal that item = a . b
    # now we consider a <= b 
    #              - a.b >= a^2
    #              - n >= a^2
    #              - a <= root under n
    # we loop from 2 to (root n) ; find a and b , multiply to check for n :)
    for a in range(2,int(math.sqrt(item)) + 1):
    
        if item % a == 0:
            result=False
            break
    return result
print(primeNormal(15))
print(primeBest(15))
