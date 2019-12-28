class WeightedGraph:
    def __init__(self):
        self.adjacanetyList ={}
    def addVertex(self,v):
        if v not in self.adjacanetyList:
            self.adjacanetyList[v] = []
        else :
            print("{} already exists".format(v))
    def addEdge(self,v1,v2,w):
        if v1 in self.adjacanetyList and v2 in self.adjacanetyList:
            self.adjacanetyList[v1].append({"node":v2,"weight":w})
            self.adjacanetyList[v2].append({"node":v1,"weight":w})
        else :
            print("vertex not present !")
