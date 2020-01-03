# this works on the fact that 10 = 2 * 5 * 1
#  to make time complexity sqrt(n) we check if d < sqrt(n) -- this is the only case we will have probability to find anything to divide
# as in the worst case loop  runs sqrt(n) times TC is O(sqrt(n))
import math
def primeFactorization(n):
    primes=[1]
    powers=[1]
    for i in range(2,n):
        if i*i > n :
            break
        exponent=0
        while(n%i == 0):
            if exponent == 0:
                primes.append(i)
            exponent +=1
            n =  n//i
            if n == 1 :
                
                break
        powers.append(exponent)
    return list(zip(primes,powers))
print(primeFactorization(6))
    
            
            

        
            
        