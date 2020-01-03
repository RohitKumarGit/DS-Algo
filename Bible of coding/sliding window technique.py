#this method finds a sub array on the basis of come give conditions

#example : we are going to build up a function which returns a sub array of maximum length having k distinct elements

def STL(arr,k):
    ans=[]
    left = 1
    p=[]
    count = 0
    i=0
   
    for s in range(1,len(arr)):
        count = 0
        i = 0
        p=[]
        while count < k :
            if arr[i] not in p:
                count+=1
            p.append(arr[i])
            i+=1
        if len(p) > len(ans):
            ans=p
        
    return ans
print(STL([1,5,2,1,7,2,7,5,5,7],4))