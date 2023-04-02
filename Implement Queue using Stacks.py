class MyQueue(object):

    def __init__(self):
        self._data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._data.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self._data.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self._data[0]

    def empty(self):
        """
        :rtype: bool
        """
        if (self._data == []):
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()