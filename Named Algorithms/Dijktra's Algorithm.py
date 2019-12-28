from pq import PriorityQueue
from pq import Node
import weighted_graph
graph=weighted_graph.WeightedGraph()
input=["A","B","C","D","E","F"]
for ins in input:
    
    graph.addVertex(ins)
graph.addEdge("A","B",4)
graph.addEdge("A","C",4)
graph.addEdge("C","D",2)
graph.addEdge("D","E",4)
graph.addEdge("B","E",3)
graph.addEdge("C","F",4)
graph.addEdge("D","F",1)
graph.addEdge("E","F",1)
m=graph.adjacanetyList
def prints(obj):
    for i in obj.values:
        
        print(i.value,end=" ")
        print(i.Priority,end=" ")
        print("\n")

# graph ccreated
def getAdjacentDistance(a,b):
    for i in graph.adjacanetyList[a]:
        if i["node"] == b:
            return i["weight"]
def calculateDistance(initial,item,vertex,previous,d):
    print("distance {} --> {}".format(item,vertex)) #item : F , vertex : C
    if item== initial:
        print("returning {}".format(getAdjacentDistance(item,vertex)))
        
        return getAdjacentDistance(item,vertex)
    
   
    
    d+=calculateDistance(initial,previous[item],item,previous,d)
    d+=getAdjacentDistance(item,vertex)
    print("returning final {}".format(d))
    return d
def algo(v1,v2,grph):
    distances ={}
    previous={}
    distances[v1]=0
    pq=PriorityQueue()
    pq.add(v1,0)
    previous[v1]=None
    for i in grph.adjacanetyList:
        if i !=v1:
            distances[i]=1000
            pq.add(i,1000)
            previous[i]=None
    print(previous)
    print(distances)
    
    
algo("A","D",graph)