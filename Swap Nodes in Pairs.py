# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        prev, cur = dummy, head

        while cur and cur.next:
            nexpair = cur.next.next
            nex = cur.next

            nex.next = cur
            cur.next = nexpair
            prev.next = nex

            prev = cur
            cur = nexpair

        return dummy.next