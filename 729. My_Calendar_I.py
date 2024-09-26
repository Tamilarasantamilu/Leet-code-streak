class MyCalendar:

    def __init__(self):
        self.book_l = []

    def book(self, start: int, end: int) -> bool:
        if len(self.book_l) == 0:
            self.book_l.append((start,end))
            return True 
        for i,j in self.book_l:
            if start < j and end > i:
                return False
        self.book_l.append((start,end))
        return True    
