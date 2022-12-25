class MyQueue:

    def __init__(self):
        self.MyQueue = []

    def push(self, x: int) -> None:
        self.MyQueue.append(x)

    def pop(self) -> int:
        return self.MyQueue.pop(0)

    def peek(self) -> int:
        copy = self.MyQueue
        return copy[0]

    def empty(self) -> bool:
        if self.MyQueue == []:
            return True
        else:
            return False