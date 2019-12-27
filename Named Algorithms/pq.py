
class Node:
    def __init__(self,v,p):
        self.value=v
        self.Priority=p
class PriorityQueue:
    def __init__(self,val,pr):
        newNode=Node(val,pr)
        self.values=[newNode]
    def getParent(self,pr):
        return (pr-1)//2
    def getRight(self,pr):
        
        return 2*pr + 2
    def getLeft(self,pr):
        
        return 2*pr + 1
    def add(self,v,pr):
        newNode=Node(v,pr)
        self.values.append(newNode)
        p=newNode.Priority
        idx=len(self.values) - 1
        while self.values[self.getParent(idx)].Priority > self.values[idx].Priority:
            
            temp=self.values[self.getParent(idx)]
            self.values[self.getParent(idx)]=self.values[idx]
            self.values[idx]=temp
            idx=self.getParent(idx)
            if idx <=0: #this is important
                break
    def toswapwith(self,idx):
        left=self.getLeft(idx)
        right=self.getRight(idx)
        if self.getLeft(idx) > len(self.values) - 1:
            return self.getRight(idx)
        if self.getRight(idx) > len(self.values) - 1:
            return self.getLeft(idx)
        return self.getRight(idx) if self.values[self.getRight(idx)] > self.values[self.getLeft(idx)] else self.getLeft(idx)
        
    def remove(self):
        temp=self.values[0]
        self.values[0]=self.values[-1]
        self.values[-1]=temp
        m=self.values.pop()
        idx=0
        im=self.toswapwith(idx)
        if im > len(self.values) - 1:
            return 0
        while self.values[self.toswapwith(idx)].Priority < self.values[idx].Priority:
            temp=self.values[self.toswapwith(idx)]
            self.values[self.toswapwith(idx)]=self.values[idx]
            self.values[idx]=temp
            idx=self.toswapwith(idx)
            
            if idx > len(self.values) - 1 or self.toswapwith(idx) > len(self.values) - 1: #important
                break
        return m
def prints(obj):
    for i in obj.values:
        print(i.value,end=" ")
        print(i.Priority,end=" ")
        print("\n")



        
