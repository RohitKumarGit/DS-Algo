a=[5,-6,3,4,-2,3,-2]
def maximumSubArray(n):
    sum=0
    ans=0
    for i in range(len(n)):
        sum += a[i]
        if sum < 0 :
            sum = 0
        if sum > ans:
            ans=sum
    return ans
print(maximumSubArray(a))
#PARTIAL SUM METHOD
def maximumSubArrayPartialSum(arr):
    sum=0
    min=0
    s=[arr[0]]
    for i in range(1,len(arr)):
        s.append(arr[i] + s[i-1])
    for i in range(len(a)):
        if s[i] - min > sum:
            sum = s[i] - min
        if s[i] < min :
            min = s[i]
    return sum
print(maximumSubArrayPartialSum(a))
    