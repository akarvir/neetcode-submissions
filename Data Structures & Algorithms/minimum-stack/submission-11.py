class MinStack:
    def __init__(self):
        self.stack = []
        self.heap = []
        self.min = float('inf')
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.heap.append(min(val,self.min))
        self.min = min(val,self.min)
    def pop(self) -> None:
        self.stack.pop()
        self.heap.pop()
        self.min = self.heap[-1] if self.heap else float('inf')
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.heap[-1]

