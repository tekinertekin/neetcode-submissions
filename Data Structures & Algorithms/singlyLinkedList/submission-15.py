class LinkedList:
    l = []
    
    def __init__(self):
        pass
    
    def get(self, index: int) -> int:
        return self.l[index] if -1 < index < len(self.l) else -1

    def insertHead(self, val: int) -> None:
        self.l = [val] + self.l

    def insertTail(self, val: int) -> None:
        self.l = self.l + [val]

    def remove(self, index: int) -> bool:
        print(self.l)
        print(index)
        print(self.l[0:index])
        print(self.l[index + 1:])
        if index < len(self.l):
            self.l = self.l[:index] + self.l[index + 1:]
            return True
        return False

    def getValues(self) -> List[int]:
        return self.l
        
