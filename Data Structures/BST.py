import random
class TreeNode:
    def __init__(self,v):
        self.left=None
        self.right = None
        self.value = v
class Tree:
    def __init__(self,v):
        self.root=TreeNode(v)
    def insert(self,value,pointer):
        newNode=TreeNode(value)
        
        
        #print("adding {}".format(value))
        if value >= pointer.value and pointer.right == None:
            pointer.right=newNode
            return 0
        elif newNode.value <= pointer.value and pointer.left == None:
            pointer.left=newNode
            return 0
        else :
            nextNode = pointer.right if pointer.value < value else pointer.left
            print(nextNode.value)
            self.insert(value,nextNode)
        return 0
    def search(self,tofind,pointer):
        
        
        if pointer == None:
            return False
        if tofind == pointer.value:
            return True
        if tofind >  pointer.value:
            
            goto = pointer.right
        if tofind < pointer.value:
            goto=pointer.left
           # ms=pointer.left.value
        
        result = self.search(tofind,goto)
        return result
    
tree=Tree(13)
input=[]
for i in range(6):
    input.append(random.randint(1,20))
input=[ 6, 8,  14, 17]
print(input)
for s in input:
    tree.insert(s,tree.root)
tree.insert(-7,tree.root)
print(tree.search(-8,tree.root))