class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.maxSize=maxSize
        self.c=0

        

    def push(self, x: int) -> None:
        if self.c==self.maxSize:
            return False
        self.stack.append(x)
        self.c+=1
        

    def pop(self) -> int:
        if self.c==0:
            return -1
        x=self.stack.pop()
        self.c-=1
        return x
        

    def increment(self, k: int, val: int) -> None:
        if self.c< k:
            for i in range(self.c):
                self.stack[i]= self.stack[i]+val
        else:
            for i in range(k):
                    self.stack[i]= self.stack[i]+val
        
        



        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)