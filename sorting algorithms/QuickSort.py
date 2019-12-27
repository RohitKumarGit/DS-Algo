"""
QUICK SORT
-we take a pivot..you got it
"""
import random
def quickSort(arr):
    if len(arr) == 1:
        return arr
    pivot=arr[0]
    l=[]
    r=[]
    left=l
    right=r
    for i in arr[1:]:
        if i < pivot:
            l.append(i)
        else :
            r.append(i)
    if len(l)>0:
        left=quickSort(l)
    if len(r)>0:
        right=quickSort(r)
    return ( left + [pivot] + right)
input=[]
for i in range(10):
    input.append(random.randint(-10,25))
print(quickSort(input))
