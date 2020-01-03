a=[3,7,1,4,2,5,6,3,8, 10 , 9]
ans=[]
result=[]
for i in range(len(a)):
    min=a[i]
    max=a[i]
    p=[a[i]]
    gotIt=False
    once=True
    for s in range(i+1,len(a)):
        if a[s] > max :
            max=a[s]
        if a[s] < min :
            min=a[s]
        p.append(a[s])
        if p.count(a[s]) > 1 :
            once=False
            break
        if once and max - min == s-i:
            gotIt=True
            ans.append(p)
            break
    if gotIt and len(p) > len(result):
        result=p
print(result)
            
    
    

