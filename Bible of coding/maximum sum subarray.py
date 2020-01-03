a=[5,-6,3,4,-2,3,-2]
#greedy approach
sum=0
ans =0
for i in range(len(a)):
    sum+=a[i]
    if sum < 0:
        sum=0
    if sum > ans:
        ans=sum
print(ans)

#partial sum approach 
#we fix oe of the pointer , in this case the right
# sum of anysub array = paartial(right) - partial(left)
# as right is constant , to make sum maximum we need to fund minumum partial(left)
# here's the code
def partialSum(array):
    partialSum =[array[0]]
    for i in range(1,len(array)):
        partialSum.append(array[i] + partialSum[i-1])
    
    return partialSum
partialSum=partialSum(a)
ans=0
min=partialSum[0]
for i in range(len(partialSum)):
    if partialSum[i] < min :
        min = partialSum[i]
    sum = partialSum[i] - min
    if sum > ans:
        ans=sum
print(ans)
    