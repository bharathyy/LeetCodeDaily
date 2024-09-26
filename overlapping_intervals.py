class MyCalendar:

    def __init__(self):
        self.starting=[]
        self.ending=[]
        
    def book(self, start: int, end: int) -> bool:
        self.starting.append(start)
        self.ending.append(end)
        
        for i in range(len(self.starting) - 1):
            prev_start = self.starting[i]
            prev_end = self.ending[i]
            
            if not (end <= prev_start or start >= prev_end):
                self.starting.pop()
                self.ending.pop()
                return False
        return True

            
            


    

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)