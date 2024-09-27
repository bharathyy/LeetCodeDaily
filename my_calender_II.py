class MyCalendarTwo:

    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []
        

    def book(self, start: int, end: int) -> bool:

        for ds,de in self.double_bookings:
            if max(ds,start)<min(de,end):
                return False
        for ss,se in self.single_bookings:
            over_s=max(start,ss)
            over_e=min(end,se)
            if over_s<over_e:
                self.double_bookings.append((over_s,over_e))
        self.single_bookings.append((start,end))

        return True
    



        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)