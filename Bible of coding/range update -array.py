def partialSum(array):
    partialSum =[array[0]]
    for i in range(1,len(array)):
        partialSum.append(array[i] + partialSum[i-1])
    
    return partialSum
    
def rangeUpdate(arr,x,y,k):
    # add k from x to y
    temp=[0 for i in arr] # constant time
    temp[x] +=k
    temp[y+1] -=k
    return temp
def build(temp,array):
    for i in range(len(temp)):
        array[i] += temp[i]
    return array
array=[1,4,2,3,3,1,4,2,4,2,3]
temp=rangeUpdate(array,1,4,2)

temp=partialSum(temp)
print(temp)
print(array)
print(build(temp,array))