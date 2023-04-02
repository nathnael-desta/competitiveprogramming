class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.data = []
        self.max = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.data) < self.max:
            self.data.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.data) < self.max:
            self.data.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.data) > 0:
            self.data.pop(0)
            return True
        else:
            return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.data) > 0:
            self.data.pop()
            return True
        else:
            return False

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.data) > 0:
            return self.data[0]
        else:
            return -1

    def getRear(self):
        """
        :rtype: int
        """
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.data) == 0:
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.data) == self.max:
            return True
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()