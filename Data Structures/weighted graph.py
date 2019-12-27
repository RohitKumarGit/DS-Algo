class Graph:
    def __init__(self,val,w):
        self.visited=[]
        self.vertex={{"node":val,"weight":w}}
    def insertVertex(self,v):
        if v not in self.vertex :
            self.vertex[v] = []
        else :
            print("the vertex is already there!")
    def insertEdge(self,v1,v2,w):
        if v1 in self.vertex and v2 in self.vertex:
            if v2 not in self.vertex[v1]:
                self.vertex[v1].append({"node":v2,"weight":w})
            if v1 not in self.vertex[v2]:
                self.vertex[v2].append({"node":v1,"weight":w})
        else :
            print("we can't do")
    def removeVertex(self,v):
        if v in self.vertex:
            del self.vertex[v]
            for m in self.vertex:
                pre=[i for i in self.vertex[m] if i !=v]
                self.vertex[m]=pre
        else :
            print("Not present")
    def removeEdge(self,v1,v2):
        self.vertex[v1].remove(v2)
        self.vertex[v2].remove(v1)
    def DFStraverseItereative(self,start):
        #we use a stack
        result=[]
        stack=[start]
        while len(stack) > 0:
            
            verte= stack.pop()
            if verte not in result:
                result.append(verte)
                print(type(verte))
                for i in self.vertex[verte]:
                    stack.append(i)
        return result
    def DFSRecursive(self,start):
        if start not in self.visited:
            self.visited.append(start)
            for i in self.vertex[start]:
                km=self.DFSRecursive(i)
                self.visited=km
        return self.visited
    def BFSsearch(self,start):
        #the only difference b/w BFS and DFS is that BFS uses 'queue' and DFS uses 'stack'
        result=[]
        stack=[start]
        while len(stack) > 0:
            
            verte= stack.pop(0)
            if verte not in result:
                result.append(verte)
                print(type(verte))
                for i in self.vertex[verte]:
                    stack.append(i)
        return result

graph=Graph("rohit")
graph.insertVertex("rajiv")
graph.insertVertex("king")
graph.insertEdge("rohit","king")
graph.insertEdge("rohit","rajiv")
#graph.removeEdge("rohit","rajiv")



print(graph.vertex)
print(graph.BFSsearch("rohit"))
                
number = int(input("enter a number"))
result=True
for i in range(1,number/2 +1):
    if number%i == 0:
        result = False
        break
print(result)