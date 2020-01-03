"""
SIEVRE OF ERASTHOMERS
"""
def getPrimes(n):
    isPrime=[True for i in range(n+1)]
    for i in range(2,n+1):
        if isPrime[i]:
            c=2*i
            while c <= len(isPrime) - 1:
                isPrime[c]=False
                c+=i
        
    result= []
    for i in range(1,n+1):
        if isPrime[i]:
            result.append(i)
    return result
print(getPrimes(8))
            
                
    