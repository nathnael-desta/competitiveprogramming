class MinStack:

    def __init__(self):
        self.MinStack = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)

    def pop(self) -> None:
        self.MinStack.pop(len(self.MinStack) - 1)

    def top(self) -> int:
        return self.MinStack[len(self.MinStack) - 1]

    def getMin(self) -> int:
        return min(self.MinStack)