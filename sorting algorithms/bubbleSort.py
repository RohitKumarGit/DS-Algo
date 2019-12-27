"""
Bubble sort
- In bubble sort we take the sorted part to the end of the array
- we can do this iteratively or recursively
- we just compare arr[j] and arr[j+1] and if arr[j] > arr[j+1] we SWAP
That's it
"""
import random
def swap(arr,i1,i2):
    temp=arr[i1]
    arr[i1]=arr[i2]
    arr[i2]=temp
def BubbleSort(arr):
    for count in range(len(arr)):
        for i in range(len(arr) -1 - count):
            j=i+1
            if arr[i] > arr[j]:
                swap(arr,i,j)
    
    return arr

input=[]
for i in range(10):
    input.append(random.randint(-10,25))
print(input)
print(BubbleSort(input))


