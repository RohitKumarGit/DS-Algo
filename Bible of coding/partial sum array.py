array=[1,4,2,3,3,1,4,2,4,2,3]
partialSum =[array[0]]
for i in range(1,len(array)):
    partialSum.append(array[i] + partialSum[i-1])
print(partialSum)
    