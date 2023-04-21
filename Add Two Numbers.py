# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = ""
        s2 = ""
        while l1 != None:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2 != None:
            s2 = str(l2.val) + s2
            l2 = l2.next
        add = str(int(str(int(s1) + int (s2))))
        res = ListNode()
        print(add)
        for i in range(len(add) - 1, -1, -1):
            new_node = ListNode(add[i])
            cur = res
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
        while res.val == 0:
            res = res.next
        return res


        print(s1,s2)