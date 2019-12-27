"""
MERGE SORT  
- we break the array recursively into singular array and then join it from back !
"""

# first let's make the merge function which merges two sorted arrays
import random
def merge(arr1,arr2):
    i=0
    j=0
    sorted=[]
    while i <= len(arr1) -1 and j <=len(arr2) -1:
        arr1pointer=arr1[i]
        arr2pointer=arr2[j]
        if arr1[i] < arr2[j]:
            sorted.append(arr1[i])
            if i == len(arr1) -1 :
                arr1.append("fuck")
                break
            i+=1
        else :
            sorted.append(arr2[j])
            if j == len(arr2) - 1:
                
                arr2.append("fuck")
                break
            j+=1
   
   
    if arr1[-1] == "fuck" :
        sorted +=arr2[j:]
    if arr2[-1] == "fuck":
        sorted +=arr1[i:]
    return sorted
#now we will define the mergeSort ()
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left = mergeSort(arr[:middle])
    right=mergeSort(arr[middle:])
    return merge(left,right)
input=[]
for i in range(10):
    input.append(random.randint(-10,25))
print(input)
print(mergeSort(input))
