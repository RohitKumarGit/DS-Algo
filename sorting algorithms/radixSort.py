"""
RADIX SORT
- THE BUCKET WAY
"""
import random
def findGreatesDig(arr):
    return max([len(str(i)) for i in arr])

def flatten(arr,res):
    if type(arr)  != list:
        return arr

    for i in arr:
        if type(i) == list:
            flatten(i,res)
        else:
            res.append(i)
    return res
def RadixSort(arr):
    s=findGreatesDig(arr)+1
    for i in range(1,s):
        m=i
        bucket=[[] for i in range(10)]
        for number in arr:
            #print(arr)
            if len(str(number)) < i:
                bucket[0].append(number)
            else :
                digit=int(str(number)[-1 * i])
         
                bucket[digit].append(number)
        print(bucket)
        res=[]
        bucket=flatten(bucket,[])
        print(bucket)
        
        arr=bucket     
         
    return arr  
input=[]
for i in range(10):
    input.append(random.randint(0,25))    
print(input)
print(RadixSort(input))
