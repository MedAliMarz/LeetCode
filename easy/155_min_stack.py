class MinStack:
        
    stack = []
    mins = [] # array to save the previous min values (after insertion)
    def __init__(self):
        self.mini = None
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(val if (len(self.stack) == 1) else val if val < self.mins[-1] else self.mins[-1])
        
    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


