# this works on the fact that 10 = 2 * 5 * 1
#  to make time complexity sqrt(n) we check if d < sqrt(n) -- this is the only case we will have probability to find anything to divide
# as in the worst case loop  runs sqrt(n) times TC is O(sqrt(n))
import math
def primeFactorization(item):
    d=2
    expo=[]
    primes=[]
    
    while item > 1 and d*d <= item:                             """
                                                                                time complexity O(sqrt(n))
                                                                        """
        k=0
        while item % d == 0:
            item = item // d
            k +=1
            
        if k > 0 :
            expo.append(k)
            primes.append(d)
        d +=1
    if item > 1:
            expo.append(1)
            primes.append(item)    
    return list(zip(primes,expo))

print(primeFactorization(15))
        

        
            
        