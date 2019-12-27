class HashMap:
    def __init__(self,l):
        self.values=[None for i in range(l)]
        self.length = l
    def hashing(self,key):
        return sum([ord(i) for i in str(key)]) % self.length
    def insert(self,key,value):
        
        hashs=self.hashing(key)
        if self.values[hashs] == None:
            self.values[hashs]=value
        elif type(self.values[hashs]) == list:
            self.values[hashs].append([key,value])
        else :
            tofill=[]
            there = self.values[hashs]
            tofill.append(there)
            tofill.append([key,value])
            self.values[hashs]=tofill
    def search(self,key):
        hashs=self.hashing(key)
        if hashs > len(self.values) - 1:
            return "Nothing here"
        item=self.values[hashs]
        if type(item) == list:
            for i in item[1:]:
                if i[0] == key:
                    return i[-1]  
            return item[0]
        else :
            return item
            


hahsmap=HashMap(3)
hahsmap.insert("rohit","student")
hahsmap.insert("rajiv","shit")
hahsmap.insert("jivar","fuck")
print(hahsmap.values)
print(hahsmap.search("rohit"))
#fucking awesome !!!

     
