"""
HEAPS - MAX-heap and MIN-heap

"""

#code for a max heap
def swap(arr,idx1,idx2):
    temp=arr[idx1]
    arr[idx1]=arr[idx2]
    arr[idx2] = temp
    return arr
class Heap:
    def __init__(self,values):
        self.values=values
    def getRight(self,idx):
        return (2*idx) + 2
    def getLeft(self,idx):
        return (2*idx) + 1
    def getParent(self,idx):
        return  (idx -1)//2
    def swapwith(self,idx):
        #will return index for extract max
        l=self.getLeft(idx)
        r=self.getRight(idx)
        if self.values[l] == self.values[r]:
            return r
        if self.values[l] > self.values[r]:
            return l
        else :
            return r
    def insert(self,value):
        self.values.append(value)
        idx=len(self.values) -1
        while self.values[self.getParent(idx)] < value:
            
            self.values=swap(self.values,self.getParent(idx),idx)
            
            idx=self.getParent(idx)
            if idx <= 0:
                break
            
    def extractMax(self):
        swap(self.values,0,len(self.values) - 1)
        self.values.pop()
        idx = 0

        while self.values[idx] < self.values[self.swapwith(idx)] :
            swap(idx,self.swapwith(idx))
            idx = self.swapwith(idx)
            if idx > len(self.values) - 1 :
                break

        return self.values
heap=Heap([2,1,4,-3,5])
heap.insert(10)
heap.extractMax()
print(heap.values)


        
