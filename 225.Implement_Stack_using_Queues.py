class MyStack:

    def __init__(self):
        self.Q1 = []
        self.Q2 = []

    def push(self, x: int) -> None:
        self.Q2.append(x)
        while len(self.Q1) > 0:
            self.Q2.append(self.Q1.pop(0))
        self.Q1, self.Q2 = self.Q2, self.Q1

    def pop(self) -> int:
        return self.Q1.pop(0)

    def top(self) -> int:
        return self.Q1[0]

    def empty(self) -> bool:
        return len(self.Q1) == 0 and len(self.Q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()