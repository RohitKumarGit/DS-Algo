array=[1,4,2,3,3,1,4,2,4,2,3]
cumuativeSUm=[array[0]]
for i in range(1,len(array)):
    
    cumuativeSUm.append(array[i] + cumuativeSUm[i-1])
# the above thing is O(n)

#now we will do he queris with O(1) :)
def sums(x,y):
    return cumuativeSUm[y] -cumuativeSUm[x] + array[x]
print(sums(2,3))