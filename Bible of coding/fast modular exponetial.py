# 2 ^4 ; 2 * 2*3; 2 * 2 * 2 ^ 2
def fastModularExponential(a,n):
    if n  == 0:
        return 1
    if n % 2 == 0:
        s=fastModularExponential(a*a,n//2)
        return  s
    return a * fastModularExponential(a,n-1)
print(fastModularExponential(2,4))