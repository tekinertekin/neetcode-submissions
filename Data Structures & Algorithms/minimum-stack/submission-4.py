class MinStack:
    s = None
    mn_s = None

    def __init__(self):
        self.s = []
        self.mn_s = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.mn_s or self.mn_s[-1] >= val:
            self.mn_s.append(val)
        else:
            self.mn_s.append(self.mn_s[-1])
        

    def pop(self) -> None:
        self.s.pop()
        self.mn_s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.mn_s[-1]
        
