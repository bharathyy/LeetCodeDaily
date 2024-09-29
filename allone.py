class AllOne:

    def __init__(self):
        self.d={}
        

    def inc(self, key: str) -> None:
        if key in self.d.keys():
            self.d[key]+=1
        else:
            self.d[key]=1
        

    def dec(self, key: str) -> None:
        if key in self.d.keys():
            if self.d[key]>1:
                self.d[key]-=1
            else:
                del self.d[key]
    

    def getMaxKey(self) -> str:
        if not self.d:
            return ""
        return max(self.d,key=self.d.get)
       

        

    def getMinKey(self) -> str:
        if not self.d:
            return ""
        return min(self.d,key=self.d.get)
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()