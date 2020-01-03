"""
SIEVRE OF ERASTHOMERS
"""
def primeNumbersUpToN(n):
    isPrime=[True for i in range(n+1)]
    for i in range(2,n + 1):
        if isPrime[i]:
            m=2*i
            while m <= n:
                isPrime[m] = False
                m +=i
    primes=[]
    for i in range(1,len(isPrime)):
        if isPrime[i]:
            primes.append(i)
    
    return primes        

print(primeNumbersUpToN(4))    