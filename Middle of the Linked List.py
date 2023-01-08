# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = head
        tortoise = head
        while hare != None and hare.next != None:
            hare = hare.next.next
            tortoise = tortoise.next
        return tortoise